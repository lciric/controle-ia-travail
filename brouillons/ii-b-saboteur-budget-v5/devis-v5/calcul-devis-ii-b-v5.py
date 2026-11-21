"""Arithmétique du devis de l'étalonnage et de la course de l'organisme retenu du saboteur à budget (v5).

Processeur seulement ; aucune donnée mesurée de la première course n'est lue : seuls ses horodatages, son prix horaire
et sa durée facturée, recopiés à la main ci-dessous depuis la branche `origin/claude/iib-executante-v1`, dossier
`registres/iib-executante/course-836c7ccc-v1/` :
- `journal-instance-61414494-v1.txt` (lignes AMORCE, PROGRES, « tests », « run ») ;
- `surveillance-20261119-085912-iib-reel-v1.txt`, ligne 1 (création, prix de la carte, prix du stockage) ;
- `journal-course-destruction-v1.txt` (création, inventaire après FIN, arrêt, destructions) ;
- `diagnostic-epreuve-E-O1-20261119-085912-iib-reel-v1.md`, lignes 173-175 (durée du run, borne de prix).
Comptes : texte scellé `conception-organisme-retenu-ii-b-v5-scellee-v1.md` (c1dc5459…), sections 10.1, 10.2, 12,
table des nœuds (nœud 7, option (b')). Bornes de la machine et des gardes : ordre scellé de la première course
(`ordre-exploratoire-ii-b-v1.md`, § 1 et § 2) et calcul du premier devis (`calcul-devis-ii-b-v3.py`).
Lancement : `python3 -I -B calcul-devis-ii-b-v5.py > sortie-calcul-devis-ii-b-v5.txt`.
"""
from __future__ import annotations

from datetime import datetime
from math import floor

# ---------- 1. Relevés de la première course (horodatages UTC du 2026-11-19, prix, durée) ----------
def t(hms: str) -> datetime:
    return datetime.strptime("2026-11-19T" + hms, "%Y-%m-%dT%H:%M:%S")

CREATION = t("08:53:52")            # journal de destruction l. 57 ; époque 1795078446 (surveillance l. 1)
DEBUT_AMORCE = t("08:54:18")        # journal de l'instance l. 1
FIN_TESTS_DEBUT_RUN = t("08:59:12") # journal de l'instance l. 17 et l. 19
DUREE_TESTS_S = 177.87              # journal de l'instance l. 17 (456 essais)
LOTS = [t(x) for x in ("09:08:15", "09:13:06", "09:17:41", "09:22:59", "09:28:31", "09:33:52", "09:38:30",
                       "09:43:45", "09:48:40", "09:53:53", "09:59:31", "10:05:34")]  # l. 20-31, 8 épisodes par lot
FIN_ORACLE = t("10:13:45")          # l. 32 : oracle de l'étalonnage fini, 96 épisodes, 960 actions d'oracle
ARRET = t("10:14:33")               # journal de destruction l. 69 : arrêt par identifiant
DESTRUCTION = t("10:20:55")         # journal de destruction l. 159
DUREE_RUN_S = 4469.3                # diagnostic l. 174, chargement du modèle compris
DUREE_FACTUREE_A_FIN_S = 4835.89    # journal de destruction, inventaire après FIN de 10:14:26Z
PRIX_CARTE_REEL, PRIX_STOCKAGE_REEL = 1.186667, 0.033333   # surveillance l. 1 ; somme 1,22 (inventaire)
EP_PAR_LOT, ACTIONS_ORACLE_1RE = 8, 960

# ---------- 2. Bornes de la machine et des gardes (ordre de la première course, § 1 et § 2) ----------
PRIX_CARTE_MAX, PRIX_STOCKAGE_MAX = 1.30, 0.08
TELECH_USD_GO, TELECH_GO_ATTENDU, TELECH_GO_PIRE = 0.05, 20, 40
ARRET_H_ATTENDU, ARRET_H_PIRE = 24, 48
CONSIGNATION_S = 2400

# ---------- 3. Comptes du texte scellé v5 ----------
T = 10                                   # actions par épisode (section 12)
ETAL_EPISODES = 64 + 64 + 32             # honnêtes, régénérés, flagrants générés (10.1) = 160
ETAL_ACTIONS_ORACLE = 640 + 640 + 640 + 640 + 640 + 320 + 320   # section 12 = 3 840
EP_PAR_TOUR, ORACLES_PAR_TOUR = 32, 1    # 10.2, nœud 7 (b')
ACTIONS_HORS_TOURS = 3520                # nœud 7 (b') : 960 + 2 560
EVAL_EPISODES, EVAL_ACTIONS_ORACLE = 256, 2560   # section 12 (800 − 160 − 384 épisodes ; 2 560 actions)
ACCEPTES_MAX, ACCEPTES_VISES_AVEC_MARGE = 96, 384   # 10.2

# ---------- 4. Hypothèses du rédacteur (aucune n'est mesurée sur l'organisme v5) ----------
DIST_S, EPOQUES = 891 / 480, 3           # distillation : premier devis (non mesurée à la première course)
FIN_COURSE_S = 360                       # écriture, scellement, poussées : 0,10 h, premier devis
FACTEUR_HOTE_PIRE = 2.0                  # hôte lent : convention du premier devis (P1)
FACTEUR_ORACLE_PIRE = 1.5                # en plus : oracles neufs ([P], [N] à réécriture couplée) jamais chronométrés
FACTEUR_FIXE_PIRE = 3.0                  # suite d'essais plus longue, modèle à retélécharger
PLAFOND_LIGNE, COUPURE = 60.0, 55.0      # proposés
PLAFOND_ETAPE1, COUPURE_ETAPE1 = 17.0, 12.0   # proposés
RESERVE_ENTREES = 5.0                    # proposée : plafond du fichier d'entrées = coupure − réserve
DEPENSE_PASSEE = 0.0                     # ligne neuve ; la dépense de la première course est sur l'ancienne ligne

_n = 0
def L(texte: str) -> None:
    global _n
    _n += 1
    print(f"[L{_n:02d}] {texte}")

def h(s: float) -> float:
    return s / 3600


def main() -> None:
    print("Devis de l'organisme retenu du saboteur à budget (v5) — arithmétique (calcul v5) ; secondes, heures, USD")

    print("\n## A. Durées, prix et dépense réels de la première course")
    durees_lots = [(b - a).total_seconds() for a, b in zip(LOTS, LOTS[1:])]
    ep_moy = sum(durees_lots) / (len(durees_lots) * EP_PAR_LOT)
    ep_min, ep_max = min(durees_lots) / EP_PAR_LOT, max(durees_lots) / EP_PAR_LOT
    lot1 = (LOTS[0] - FIN_TESTS_DEBUT_RUN).total_seconds()
    charge = lot1 - EP_PAR_LOT * ep_moy
    oracle_tot = (FIN_ORACLE - LOTS[-1]).total_seconds()
    act = oracle_tot / ACTIONS_ORACLE_1RE
    avant_run = (FIN_TESTS_DEBUT_RUN - CREATION).total_seconds()
    fin_arret = (ARRET - FIN_ORACLE).total_seconds()
    L(f"épisode généré : lots 2 à 12, {len(durees_lots) * EP_PAR_LOT} épisodes en {sum(durees_lots):.0f} s → {ep_moy:.2f} s par épisode "
      f"(lot le plus court {ep_min:.1f} s, le plus long {ep_max:.1f} s par épisode ; hypothèse du premier devis : 43,3 s)")
    L(f"lot 1 : {lot1:.0f} s pour 8 épisodes → chargement du modèle déduit : {charge:.0f} s")
    L(f"action d'oracle : {ACTIONS_ORACLE_1RE} actions en {oracle_tot:.0f} s → {act:.3f} s par action "
      f"(hypothèses du premier devis : 0,5 / 1,0 / 1,5 s ; pire 3,0 s)")
    L(f"de la création au début du run : {avant_run:.0f} s (dont suite d'essais {DUREE_TESTS_S:.0f} s) ; de la fin de l'oracle à l'arrêt : {fin_arret:.0f} s")
    L(f"contrôle : run {DUREE_RUN_S:.1f} s relevé ; début du run → fin de l'oracle = {(FIN_ORACLE - FIN_TESTS_DEBUT_RUN).total_seconds():.0f} s")
    prix_reel = PRIX_CARTE_REEL + PRIX_STOCKAGE_REEL
    fact = DUREE_FACTUREE_A_FIN_S + (ARRET - t("10:14:26")).total_seconds()
    dep = fact * prix_reel / 3600 + (DESTRUCTION - ARRET).total_seconds() * PRIX_STOCKAGE_REEL / 3600
    L(f"prix réel : carte {PRIX_CARTE_REEL} + stockage {PRIX_STOCKAGE_REEL} = {prix_reel:.2f} USD/h ; borne de l'ordre : "
      f"{PRIX_CARTE_MAX} + {PRIX_STOCKAGE_MAX} = {PRIX_CARTE_MAX + PRIX_STOCKAGE_MAX:.2f} USD/h")
    L(f"dépense de la première course, recalculée (non lue sur une facture) : {fact:.0f} s facturées × {prix_reel:.2f} "
      f"+ stockage à l'arrêt {(DESTRUCTION - ARRET).total_seconds():.0f} s = {dep:.2f} USD (ligne GO-2026-11-10-08, pas la ligne neuve)")

    # jeux de durées
    fixe_avant = avant_run + charge
    att = dict(nom="attendu", ep=ep_moy, act=act, fixe=fixe_avant, fin=FIN_COURSE_S, dist=DIST_S,
               prix=prix_reel, arret_h=ARRET_H_ATTENDU, st_arret=PRIX_STOCKAGE_REEL, go=TELECH_GO_ATTENDU)
    haut = dict(nom="haut", ep=ep_max, act=act * 1.5, fixe=fixe_avant * 1.5, fin=FIN_COURSE_S, dist=DIST_S * 1.3,
                prix=PRIX_CARTE_MAX + PRIX_STOCKAGE_MAX, arret_h=ARRET_H_ATTENDU, st_arret=PRIX_STOCKAGE_MAX, go=TELECH_GO_ATTENDU)
    pire = dict(nom="pire", ep=ep_moy * FACTEUR_HOTE_PIRE, act=act * FACTEUR_HOTE_PIRE * FACTEUR_ORACLE_PIRE,
                fixe=fixe_avant * FACTEUR_FIXE_PIRE, fin=FIN_COURSE_S * FACTEUR_HOTE_PIRE, dist=DIST_S * FACTEUR_HOTE_PIRE,
                prix=PRIX_CARTE_MAX + PRIX_STOCKAGE_MAX, arret_h=ARRET_H_PIRE, st_arret=PRIX_STOCKAGE_MAX, go=TELECH_GO_PIRE)

    print("\n## B. Durées unitaires retenues")
    for s in (att, haut, pire):
        L(f"{s['nom']} : épisode {s['ep']:.2f} s ; action d'oracle {s['act']:.3f} s ; fixe avant le premier épisode {s['fixe']:.0f} s ; "
          f"distillation {s['dist']:.2f} s par transcription et par époque ; prix {s['prix']:.2f} USD/h ; "
          f"à l'arrêt {s['arret_h']} h à {s['st_arret']} USD/h ; téléchargement {s['go']} Go")

    def apres(s: dict) -> float:   # stockage à l'arrêt + téléchargement
        return s["arret_h"] * s["st_arret"] + s["go"] * TELECH_USD_GO

    def etal_s(s: dict) -> float:
        return s["fixe"] + ETAL_EPISODES * s["ep"] + ETAL_ACTIONS_ORACLE * s["act"]

    def tour_s(s: dict) -> float:
        return EP_PAR_TOUR * (s["ep"] + T * s["act"] * ORACLES_PAR_TOUR)

    def fixe_course_s(s: dict) -> float:   # évaluation à un oracle + distillation (élève et témoin-jumeau) + fin
        return (EVAL_EPISODES * s["ep"] + EVAL_ACTIONS_ORACLE * s["act"]
                + 2 * ACCEPTES_MAX * EPOQUES * s["dist"] + 36 + s["fin"])

    def hors_tours_s(s: dict) -> float:
        return ACTIONS_HORS_TOURS * s["act"]

    print("\n## C. Étape 1 — l'étalonnage (deux oracles)")
    L(f"appels : {ETAL_EPISODES} épisodes générés ({ETAL_EPISODES * T} actions générées) ; {ETAL_ACTIONS_ORACLE} actions d'oracle, "
      f"soit {ETAL_ACTIONS_ORACLE} préremplissages et {ETAL_ACTIONS_ORACLE * 8} suites de 16 jetons au plus")
    for s in (att, haut, pire):
        e = etal_s(s)
        L(f"{s['nom']} : {e:.0f} s = {h(e):.2f} h (fixe {h(s['fixe']):.2f} ; épisodes {h(ETAL_EPISODES * s['ep']):.2f} ; "
          f"oracles {h(ETAL_ACTIONS_ORACLE * s['act']):.2f}) ; carte et stockage {h(e) * s['prix']:.2f} USD ; "
          f"si la course ne part pas : + arrêt et téléchargement {apres(s):.2f} → {h(e) * s['prix'] + apres(s):.2f} USD")
    px = PRIX_CARTE_MAX + PRIX_STOCKAGE_MAX
    dispo1 = (COUPURE_ETAPE1 - TELECH_GO_PIRE * TELECH_USD_GO) / px
    consig = CONSIGNATION_S / 3600 * px
    L(f"coupure proposée de l'étape 1 : {COUPURE_ETAPE1:.0f} USD → {dispo1:.2f} h de carte à {px:.2f} USD/h (40 Go déduits) ; "
      f"marge sur le pire ({h(etal_s(pire)):.2f} h) : {dispo1 - h(etal_s(pire)):.2f} h")
    tenu1 = COUPURE_ETAPE1 + consig + ARRET_H_PIRE * PRIX_STOCKAGE_MAX
    L(f"plafond proposé de l'étape 1 : {PLAFOND_ETAPE1:.0f} USD ; tenu par les gardes : {COUPURE_ETAPE1:.0f} + consignation ≤ {consig:.2f} "
      f"+ stockage à l'arrêt 48 h {ARRET_H_PIRE * PRIX_STOCKAGE_MAX:.2f} = {tenu1:.2f} USD ; marge {PLAFOND_ETAPE1 - tenu1:.2f}")

    print("\n## D. Étape 2 — la course (si la règle de désignation dit « part »), même location que l'étalonnage")
    L(f"appels par tour : {EP_PAR_TOUR} épisodes générés, {EP_PAR_TOUR * T * ORACLES_PAR_TOUR} actions d'oracle ; hors tours : "
      f"{ACTIONS_HORS_TOURS} actions d'oracle ; évaluation : {EVAL_EPISODES} épisodes générés, {EVAL_ACTIONS_ORACLE} actions d'oracle ; "
      f"distillation : 2 × {ACCEPTES_MAX} transcriptions × {EPOQUES} époques au plus")
    for tours in (6, 12, 24):
        L(f"appels de la course à {tours} tours (étalonnage non compris) : {tours * EP_PAR_TOUR + EVAL_EPISODES} épisodes générés ; "
          f"{tours * EP_PAR_TOUR * T + EVAL_ACTIONS_ORACLE + ACTIONS_HORS_TOURS} actions d'oracle "
          f"(avec l'étalonnage : {ETAL_EPISODES + tours * EP_PAR_TOUR + EVAL_EPISODES} et "
          f"{ETAL_ACTIONS_ORACLE + tours * EP_PAR_TOUR * T + EVAL_ACTIONS_ORACLE + ACTIONS_HORS_TOURS})")
    for s in (att, haut, pire):
        L(f"{s['nom']} : un tour {tour_s(s):.0f} s = {h(tour_s(s)):.3f} h, {h(tour_s(s)) * s['prix']:.3f} USD ; "
          f"coût fixe (évaluation, distillation, fin) {h(fixe_course_s(s)):.2f} h, {h(fixe_course_s(s)) * s['prix']:.2f} USD ; "
          f"actions hors tours {h(hors_tours_s(s)):.2f} h, {h(hors_tours_s(s)) * s['prix']:.2f} USD")
    for s in (att, haut, pire):
        for tours in (6, 12, 24):
            c = tours * tour_s(s) + fixe_course_s(s) + hors_tours_s(s)
            tout = etal_s(s) + c
            L(f"{s['nom']}, {tours} tours : course seule {h(c):.2f} h, {h(c) * s['prix']:.2f} USD ; avec l'étalonnage {h(tout):.2f} h, "
              f"{h(tout) * s['prix']:.2f} USD ; plus arrêt et téléchargement {apres(s):.2f} → total {h(tout) * s['prix'] + apres(s):.2f} USD")

    print("\n## E. Points d'arrêt (liste d'arrêt, section 15), cumul depuis la création, arrêt et téléchargement compris")
    for s in (att, pire):
        e = etal_s(s)
        t4 = e + 4 * tour_s(s)
        for tours in (12, 24):
            fin_m = e + tours * tour_s(s)
            L(f"{s['nom']} : fin de l'étalonnage {h(e):.2f} h, {h(e) * s['prix'] + apres(s):.2f} USD ; tour de contrôle (tour 4) "
              f"{h(t4):.2f} h, {h(t4) * s['prix'] + apres(s):.2f} USD ; fin de {tours} tours, moins de 48 acceptés "
              f"{h(fin_m):.2f} h, {h(fin_m) * s['prix'] + apres(s):.2f} USD")

    print("\n## F. Plafond et coupure proposés de la ligne (étalonnage et course ensemble)")
    for prix in (prix_reel, px):
        dispo = (COUPURE - TELECH_GO_PIRE * TELECH_USD_GO) / prix
        L(f"coupure {COUPURE:.0f} USD à {prix:.2f} USD/h (40 Go déduits) : {dispo:.1f} h de carte")
    tenu = COUPURE + consig + ARRET_H_PIRE * PRIX_STOCKAGE_MAX
    L(f"plafond tenu par les gardes : {COUPURE:.0f} + consignation ≤ {consig:.2f} + stockage à l'arrêt 48 h "
      f"{ARRET_H_PIRE * PRIX_STOCKAGE_MAX:.2f} = {tenu:.2f} USD ; sous la ligne de {PLAFOND_LIGNE:.0f} : "
      f"{'oui' if tenu <= PLAFOND_LIGNE else 'NON'}, marge {PLAFOND_LIGNE - tenu:.2f} ; heures d'arrêt au plus : "
      f"{(PLAFOND_LIGNE - COUPURE - consig) / PRIX_STOCKAGE_MAX:.0f} h")

    print("\n## G. Plafond de tours (10.2, nœud 7 (b')) : partie entière de (plafond − dépense passée − étalonnage − coût fixe − hors tours) / tour")
    print("   coût fixe du fichier d'entrées = évaluation à un oracle + distillation + fin + téléchargement de 40 Go (2,00 USD)")
    for plafond_entrees in (COUPURE - RESERVE_ENTREES, COUPURE):
        for s in (att, haut, pire):
            fixe = h(fixe_course_s(s)) * s["prix"] + TELECH_GO_PIRE * TELECH_USD_GO
            num = plafond_entrees - DEPENSE_PASSEE - h(etal_s(s)) * s["prix"] - fixe - h(hors_tours_s(s)) * s["prix"]
            r = floor(num / (h(tour_s(s)) * s["prix"]))
            k_min = next((k for k in range(1, 65) if -(-ACCEPTES_VISES_AVEC_MARGE // k) <= r), None)
            duree = h(etal_s(s) + r * tour_s(s) + fixe_course_s(s) + hors_tours_s(s))
            L(f"plafond du fichier d'entrées {plafond_entrees:.0f} USD, durées « {s['nom']} » : ({plafond_entrees:.0f} − {DEPENSE_PASSEE:.0f} − "
              f"{h(etal_s(s)) * s['prix']:.2f} − {fixe:.2f} − {h(hors_tours_s(s)) * s['prix']:.2f}) / {h(tour_s(s)) * s['prix']:.3f} "
              f"→ {r} tours ; R = 384 / k_R tient sous ce plafond dès k_R ≥ {k_min} sur 64 ; durée de carte à ce plafond {duree:.1f} h")
    L(f"rappel : R le plus petit possible = 384 / 64 = {ACCEPTES_VISES_AVEC_MARGE // 64} tours ; la simulation du texte scellé suppose 24 tours")

    print("\n## H. Variante : deux locations (étalonnage, puis course sur une machine neuve)")
    for s in (att, pire):
        sup = h(s["fixe"]) * s["prix"] + apres(s)
        L(f"{s['nom']} : + un second fixe {h(s['fixe']):.2f} h et un second arrêt-téléchargement = + {sup:.2f} USD")


if __name__ == "__main__":
    main()
