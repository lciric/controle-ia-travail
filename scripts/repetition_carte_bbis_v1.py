"""Répétition sur carte de l'étape B bis, **données synthétiques seulement**, avant `CODE-BBIS` (mot de Lazar, R-2802 : écart
déclaré au texte scellé ; sous la ligne GO-2026-11-14-09, plafond de la répétition 3 USD, une seule machine), v1.

Aucune donnée ni sortie de 7a, 7b, T0.7 ou P3-bis n'est lue : les jetons sont tirés ici. Le code de la course n'est pas changé :
ce script **appelle** `t07bbis.apprentissage_carte_v1` (`LotCarte`, `entrainer`, `controle_carte_processeur`),
`harnais.modeles.regler_determinisme` et les constantes de la garde de débit (`t07bbis.validation_imbriquee_v1`,
`t07bbis.commun_v1`), tels quels.

Sous-commandes :
- `carte --sortie F.json [--appareil cuda] [--actions 640] [--largeur 4096] [--par-famille 3] [--tolerance 1e-4]` (sur la
  machine, par `scripts/amorce_repetition_bbis_v1.sh`) : jeu synthétique **de la taille de la course** par défaut (640 actions =
  32 tâches × 20 actions, longueurs de 150 à 297 jetons, ≈ 143 000 jetons × 4 096 dimensions : `devis-etape-b-bis-v3.md`, l. 17,
  `9431d300…` ; 1 fil de calcul comme la course, `prereg/T0.6-organismes-config-7b-v1.json`, `"fils": 1`, `b7a5c1ba…`) ;
  algorithmes déterministes (`regler_determinisme(1, appareil)`) ; apprentissages entrelacés des deux familles (couche 15,
  régularisations de la grille), durée de chacun ; déterminisme (premier réglage de chaque famille réappris : paramètres égaux au
  bit près) ; **contrôle carte-processeur** de chaque famille au seuil du texte (10⁻⁴, 256 actions de contrôle tirées à part) ;
  projection de la garde de débit de la course (2 460 apprentissages ; variante (r1) : 1 240) à partir de la médiane mesurée.
  Codes fermés : 0 réussie ; 2 garde (arguments, carte absente, tolérance au-dessus du texte) ; 8 erreur d'apprentissage (torch
  compris) ; 9 contrôle carte-processeur au-delà du seuil ou apprentissage non déterministe. Le fichier de sortie est écrit dans
  tous les cas (état, motif, durées) ; **aucune aire** (rien n'est noté).
- `offre FICHIER.json ID PRIX_USD_H` ; `garde-commande ECHEANCE_UTC_S PRIX_USD_H FEU MAINTENANT` ; `depense CUMUL PRIX` ;
  `identifiant ID` ; `absence ID TEMOIN LISTE.json` (côté session, par `scripts/lancer_repetition_bbis_v1.sh`). Code 0 accepté,
  2 refus (motif écrit).

Graines (R9) : `numpy.random.SeedSequence(ENTROPIE_REPETITION, spawn_key=(cle_de_tache(clé),))`, clés
`bbis/repetition/donnees`, `bbis/repetition/controle`, `bbis/repetition/sonde/<famille>/<l2>` ; entropie fixe écrite ici
(répétition non décisive, déclaré).
"""
from __future__ import annotations

import argparse
import json
import sys
import time
import traceback
from pathlib import Path

GO_ID = "GO-2026-11-14-09"
MOT_REPETITION = "R-2802"
PLAFOND_USD = 3.0
QUART_D_HEURE = 0.25
ECHEANCE_MAX_S = 3 * 3600
ETIQUETTE = "bbis-t07-repetition-v1"
OFFRE_MIN = {"coeurs": 16, "memoire_vive_mo": 128000, "disque_go": 60, "stockage_max_usd_h": 0.08, "prix_max_usd_h": 1.40}
# instances d'autres sessions (mot de la mère, R-2789 et la demande de la répétition) : jamais détruites ; témoins permis
INSTANCES_D_AUTRES_SESSIONS = ("58936096", "58936099", "58936100", "60480302", "60599797", "60670453")
ENTROPIE_REPETITION = 0x6B0B1D5E2C4A48F1A3E7D2C9B85F0141
ACTIONS, LARGEUR, LONGUEURS = 640, 4096, (150, 297)
COUCHE = 15
CODES = {"reussie": 0, "garde": 2, "apprentissage": 8, "controle": 9}


class Refus(Exception):
    """Refus d'une garde de la répétition (motif écrit, code 2)."""


# ------------------------------------------------------------------------------------------------------------ côté session

def exiger_offre(offre: dict, identifiant: str, prix: float) -> dict:
    """Machine de la classe de la course (A100 SXM4 80 Go ; jamais de H200), étiquette de la répétition, identifiant et prix
    relevés le jour (prix au plus celui du pire cas du devis de B bis, 1,40 USD de l'heure)."""
    fautes = []
    nom = str(offre.get("carte", "")).upper()
    if "H200" in nom or not ("A100" in nom and "80" in nom and "SXM" in nom):
        fautes.append(f"carte {offre.get('carte')!r} : A100 SXM4 80 Go attendue (celle de la course)")
    for cle in ("coeurs", "memoire_vive_mo", "disque_go"):
        try:
            v = float(offre.get(cle))
        except (TypeError, ValueError):
            v = -1.0
        if v < OFFRE_MIN[cle]:
            fautes.append(f"{cle} {offre.get(cle)!r} < {OFFRE_MIN[cle]}")
    try:
        st = float(offre.get("stockage_usd_h"))
    except (TypeError, ValueError):
        st = float("inf")
    if not st <= OFFRE_MIN["stockage_max_usd_h"]:
        fautes.append(f"stockage {offre.get('stockage_usd_h')!r} USD/h > {OFFRE_MIN['stockage_max_usd_h']}")
    if offre.get("etiquette") != ETIQUETTE:
        fautes.append(f"étiquette {offre.get('etiquette')!r} ≠ {ETIQUETTE}")
    if not str(identifiant).isdigit() or str(offre.get("id")) != str(identifiant):
        fautes.append(f"identifiant {offre.get('id')!r} de l'offre décrite ≠ offre demandée {identifiant!r}")
    try:
        p_offre = float(offre.get("prix_usd_h"))
    except (TypeError, ValueError):
        p_offre = float("nan")
    if not (0 < float(prix) <= OFFRE_MIN["prix_max_usd_h"]) or p_offre != float(prix):
        fautes.append(f"prix {prix!r} USD/h (offre : {offre.get('prix_usd_h')!r}) : relevé du jour, au plus "
                      f"{OFFRE_MIN['prix_max_usd_h']} USD/h")
    if fautes:
        raise Refus("offre hors des bornes de la répétition : " + " ; ".join(fautes))
    return offre


MARGE_USD = 0.40       # stockage (≤ 0,08 USD/h) et téléchargements (≤ 0,05 USD par Go, ≈ 5 Go) : bornes du devis de B bis


def duree_max_h(prix: float) -> float:
    """Durée de carte au plus jusqu'à l'échéance : (durée + un quart d'heure) × prix + marge < plafond, et au plus 3 h."""
    return min(ECHEANCE_MAX_S / 3600.0, (PLAFOND_USD - MARGE_USD) / float(prix) - QUART_D_HEURE)


def garde_commande(echeance: int, prix: float, feu: str, maintenant: int) -> dict:
    """Feu écrit de la mère portant la ligne de GO et le mot de la répétition ; échéance (minuterie de destruction) dans
    ]maintenant, maintenant + `duree_max_h(prix)`] : la carte jusqu'à l'échéance, plus un quart d'heure, plus la marge de
    stockage et de téléchargement, reste sous le plafond de 3 USD."""
    if not (isinstance(feu, str) and GO_ID in feu and MOT_REPETITION in feu):
        raise Refus(f"feu écrit de la mère portant {GO_ID} et {MOT_REPETITION} absent : aucune création")
    if not 0 < float(prix) <= OFFRE_MIN["prix_max_usd_h"]:
        raise Refus(f"prix {prix!r} USD/h hors de ]0 ; {OFFRE_MIN['prix_max_usd_h']}]")
    duree_h, dmax = (int(echeance) - int(maintenant)) / 3600.0, duree_max_h(prix)
    if not 0 < duree_h <= dmax:
        raise Refus(f"échéance dans {duree_h:.2f} h : au plus {dmax:.2f} h à {float(prix):g} USD/h (échéance au plus "
                    f"{int(maintenant) + int(dmax * 3600)}, plafond {PLAFOND_USD:g} USD)")
    cout = (duree_h + QUART_D_HEURE) * float(prix) + MARGE_USD
    return {"duree_h": duree_h, "cout_max_usd": cout, "plafond_usd": PLAFOND_USD, "duree_max_h": dmax}


def garde_depense(cumul: float, prix: float) -> dict:
    """Garde de dépense de la course (`registre_bbis_v1.garde_depense`), appelée telle quelle à la coupure de 3 USD."""
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
    from controle_ia.gardes import GardeArret
    from controle_ia.t07bbis.registre_bbis_v1 import garde_depense as gd
    try:
        return gd(float(cumul), float(prix), coupure=PLAFOND_USD)
    except GardeArret as e:
        raise Refus(f"{e} (répétition : plafond {PLAFOND_USD:g} USD)") from None


def exiger_identifiant(ident: str) -> str:
    ident = str(ident)
    if not ident.isdigit():
        raise Refus(f"identifiant {ident!r} illisible (destruction par l'identifiant seulement, R10)")
    if ident in INSTANCES_D_AUTRES_SESSIONS:
        raise Refus(f"instance {ident} d'une autre session : jamais détruite")
    return ident


def exiger_absence(liste, ident: str, temoin: str) -> dict:
    """Destruction prouvée par l'absence dans la liste lue sans erreur, témoin présent (`registre_bbis_v1.exiger_absence` de la
    course, appelée telle quelle après la garde d'identifiant de la répétition)."""
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
    from controle_ia.gardes import GardeArret
    from controle_ia.t07bbis.registre_bbis_v1 import exiger_absence as ea
    exiger_identifiant(ident)
    try:
        return ea(liste, ident, temoin)
    except GardeArret as e:
        raise Refus(str(e)) from None


# ------------------------------------------------------------------------------------------------------------ sur la carte

def _graine(cle: str):
    import numpy as np
    from controle_ia.manifeste import cle_de_tache
    return np.random.SeedSequence(ENTROPIE_REPETITION, spawn_key=(cle_de_tache(cle),))


def jeu_synthetique(n_actions: int, largeur: int, cle: str):
    """Actions synthétiques (jetons × largeur, simple précision comme les activations relues), deux classes égales ; un léger
    décalage des positifs le long d'une direction tirée (la sonde apprend quelque chose ; aucune aire n'est calculée)."""
    import numpy as np
    rng = np.random.default_rng(_graine(cle))
    u = rng.standard_normal(largeur).astype(np.float32)
    u /= np.linalg.norm(u)
    y = np.r_[np.ones(n_actions // 2, int), np.zeros(n_actions - n_actions // 2, int)]
    seqs = []
    for k in range(n_actions):
        n = int(rng.integers(LONGUEURS[0], LONGUEURS[1] + 1))
        x = rng.standard_normal((n, largeur), dtype=np.float32)
        if y[k]:
            x[: max(1, n // 4)] += 0.5 * u
        seqs.append(x)
    return seqs, y


def jouer_carte(sortie: Path, appareil: str = "cuda", n_actions: int = ACTIONS, largeur: int = LARGEUR, par_famille: int = 3,
                tolerance: float | None = None) -> int:
    debut = time.time()
    doc = {"texte": "prereg/T0.7-etape-B-bis-v1.md", "mot": MOT_REPETITION, "go": GO_ID, "donnees": "synthétiques seulement",
           "appareil": appareil, "actions": int(n_actions), "largeur": int(largeur), "longueurs": list(LONGUEURS),
           "fraction_de_la_course": None, "par_famille": int(par_famille), "aucune_aire": True, "etat": "en cours"}
    sortie = Path(sortie)
    if sortie.exists():
        print(f"BBIS REPETITION REFUS : {sortie} existe déjà (R12)")
        return CODES["garde"]

    def ecrire(etat: str, code: int, motif: str | None = None, pile: str | None = None) -> int:
        doc.update({"etat": etat, "code": code, "motif": motif, "pile": pile, "duree_totale_s": time.time() - debut})
        sortie.write_text(json.dumps(doc, indent=1, ensure_ascii=False, sort_keys=True, default=str) + "\n", encoding="utf-8")
        print(f"BBIS REPETITION {etat.upper()} (code {code})" + (f" : {motif}" if motif else ""))
        return code

    try:
        sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
        import numpy as np
        from controle_ia.gardes import GardeArret
        from controle_ia.harnais.modeles import regler_determinisme
        from controle_ia.t07bbis import apprentissage_carte_v1 as ac
        from controle_ia.t07bbis import validation_imbriquee_v1 as vi
        from controle_ia.t07bbis.commun_v1 import (COUCHES_REELLES, FAMILLES, L2, N_ACTIONS_CONTROLE_CARTE, N_PLIS_INTERNES,
                                                   N_REETIQUETAGES, TOLERANCE_CARTE, VARIANTES, grille)
    except Exception as e:                                         # environnement incomplet : écrit, jamais une chute
        return ecrire("garde", CODES["garde"], f"import : {type(e).__name__}: {e}", traceback.format_exc()[-4000:])
    tol = TOLERANCE_CARTE if tolerance is None else float(tolerance)
    if not 0 < tol <= TOLERANCE_CARTE or int(par_famille) < 1 or int(par_famille) > len(L2) or int(n_actions) < 8:
        return ecrire("garde", CODES["garde"], f"tolérance {tol:g} (au plus celle du texte, {TOLERANCE_CARTE:g}), "
                      f"par famille {par_famille} (1 à {len(L2)}), actions {n_actions} (au moins 8)")
    doc.update({"tolerance": tol, "fraction_de_la_course": int(n_actions) * int(largeur) / (ACTIONS * LARGEUR)})
    try:
        doc["determinisme"] = regler_determinisme(1, appareil)
    except GardeArret as e:
        return ecrire("garde", CODES["garde"], f"réglages de la carte : {e}")
    etape = "jeu synthétique"
    try:
        t0 = time.perf_counter()
        seqs, y = jeu_synthetique(int(n_actions), int(largeur), "bbis/repetition/donnees")
        ctrl, _ = jeu_synthetique(min(N_ACTIONS_CONTROLE_CARTE, 4 * int(n_actions)), int(largeur), "bbis/repetition/controle")
        doc["jetons"] = int(sum(len(s) for s in seqs))
        doc["duree_jeu_s"] = time.perf_counter() - t0
        etape = "lot sur l'appareil"
        t0 = time.perf_counter()
        lot = ac.LotCarte(seqs, appareil)
        doc["duree_lot_s"] = time.perf_counter() - t0
        reglages = [r for r in grille([COUCHE], FAMILLES) if r["l2"] in L2[: int(par_famille)]]   # entrelacés : L, A, L, A…
        doc["apprentissages"], sondes = [], {}
        etape = "apprentissages"
        for r in reglages:
            g = int(_graine(f"bbis/repetition/sonde/{r['famille']}/{r['l2']}").generate_state(1)[0])
            t0 = time.perf_counter()
            s = ac.entrainer(lot, r["famille"], r["nom"], r["couche"], y, r["l2"], g)
            doc["apprentissages"].append({"reglage": r["nom"], "famille": r["famille"], "duree_s": time.perf_counter() - t0})
            sondes.setdefault(r["famille"], (r, g, s))
        etape = "déterminisme"
        doc["deterministe"] = {}
        for f, (r, g, s) in sondes.items():
            s2 = ac.entrainer(lot, r["famille"], r["nom"], r["couche"], y, r["l2"], g)
            egal = bool(np.array_equal(s.w, s2.w) and s.b == s2.b and (s.q is None or np.array_equal(s.q, s2.q)))
            doc["deterministe"][f] = egal
        durees = [a["duree_s"] for a in doc["apprentissages"]]
        med = float(np.median(durees))
        med_lin = float(np.median([a["duree_s"] for a in doc["apprentissages"] if a["famille"] == "lineaire"]))
        total = vi.apprentissages_prevus(5, len(grille(COUCHES_REELLES, FAMILLES)), N_PLIS_INTERNES, N_REETIQUETAGES)
        total_r1 = vi.apprentissages_prevus(5, len(grille(COUCHES_REELLES, VARIANTES["r1"]["familles"])), N_PLIS_INTERNES,
                                            VARIANTES["r1"]["n_reetiquetages"])
        proj = lambda n, m, relecture: relecture + (n - vi.N_PREMIERS) * m * vi.FACTEUR_DEBIT / 3600.0 + vi.MARGE_H
        doc["garde_de_debit"] = {
            "mediane_s": med, "mediane_lineaire_s": med_lin, "apprentissages_course": total, "apprentissages_r1": total_r1,
            "limite_h": vi.LIMITE_H, "relecture_h_devis": [0.35, 0.55],
            "projete_h": [proj(total, med, h) for h in (0.35, 0.55)],
            "projete_r1_h": [proj(total_r1, med_lin, h) for h in (0.35, 0.55)],
            "mediane_seuil_s": (vi.LIMITE_H - 0.55 - vi.MARGE_H) * 3600.0 / ((total - vi.N_PREMIERS) * vi.FACTEUR_DEBIT),
            "note": "durées au lot entier de 640 actions (sonde finale, nul) ; la validation interne apprend sur 480 : prudent"}
        doc["garde_de_debit"]["se_declencherait"] = max(doc["garde_de_debit"]["projete_h"]) > vi.LIMITE_H
        etape = "contrôle carte-processeur"
        doc["controle_carte_processeur"] = {}
        for f, (r, g, s) in sondes.items():
            t0 = time.perf_counter()
            try:
                c = ac.controle_carte_processeur(s, seqs, y, r, g, ctrl, tolerance=tol)
            except GardeArret as e:
                doc["controle_carte_processeur"][f] = {"refus": str(e), "duree_s": time.perf_counter() - t0}
                return ecrire("controle", CODES["controle"], f"{f} : {e}")
            c["duree_s"] = time.perf_counter() - t0
            doc["controle_carte_processeur"][f] = c
        if not all(doc["deterministe"].values()):
            return ecrire("controle", CODES["controle"], f"apprentissage non déterministe : {doc['deterministe']}")
    except Exception as e:                                         # torch compris : arrêt écrit, code fermé
        return ecrire("apprentissage", CODES["apprentissage"], f"{etape} : {type(e).__name__}: {e}"[:4000],
                      traceback.format_exc()[-6000:])
    return ecrire("reussie", CODES["reussie"])


# ------------------------------------------------------------------------------------------------------------ entrée

def main(argv=None) -> int:
    a = list(sys.argv[1:] if argv is None else argv)
    if a[:1] == ["carte"]:
        ap = argparse.ArgumentParser(description="répétition sur carte de B bis (données synthétiques)")
        ap.add_argument("--sortie", required=True)
        ap.add_argument("--appareil", default="cuda")
        ap.add_argument("--actions", type=int, default=ACTIONS)
        ap.add_argument("--largeur", type=int, default=LARGEUR)
        ap.add_argument("--par-famille", type=int, default=3)
        ap.add_argument("--tolerance", type=float, default=None)
        x = ap.parse_args(a[1:])
        return jouer_carte(Path(x.sortie), x.appareil, x.actions, x.largeur, x.par_famille, x.tolerance)
    try:
        if a[:1] == ["offre"] and len(a) == 4:
            exiger_offre(json.loads(Path(a[1]).read_text(encoding="utf-8")), a[2], float(a[3]))
            print("BBIS REPETITION OFFRE ACCEPTEE")
        elif a[:1] == ["garde-commande"] and len(a) == 5:
            r = garde_commande(int(a[1]), float(a[2]), a[3], int(a[4]))
            print(f"BBIS REPETITION COMMANDE PERMISE : {r['duree_h']:.2f} h au plus, {r['cout_max_usd']:.2f} USD au plus")
        elif a[:1] == ["depense"] and len(a) == 3:
            print(f"BBIS REPETITION DEPENSE {garde_depense(float(a[1]), float(a[2]))}")
        elif a[:1] == ["identifiant"] and len(a) == 2:
            print(f"BBIS REPETITION IDENTIFIANT {exiger_identifiant(a[1])}")
        elif a[:1] == ["absence"] and len(a) == 4:
            try:
                liste = json.loads(Path(a[3]).read_text(encoding="utf-8"))
            except (OSError, ValueError) as e:
                raise Refus(f"absence non prouvée : liste des instances illisible ({type(e).__name__}) : arrêt") from None
            r = exiger_absence(liste, a[1], a[2])
            print(f"BBIS DESTRUCTION PROUVEE {r['detruite']} : absente de la liste, témoin {r['temoin']} présent, "
                  f"{r['instances_listees']} instance(s) listée(s)")
        else:
            print("BBIS REPETITION REFUS : commande inconnue (carte … | offre FICHIER ID PRIX | garde-commande ECHEANCE PRIX FEU "
                  "MAINTENANT | depense CUMUL PRIX | identifiant ID | absence ID TEMOIN LISTE.json)")
            return 2
    except (Refus, ValueError, OSError) as e:
        print(f"BBIS REPETITION REFUS : {e}")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
