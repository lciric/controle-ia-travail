#!/usr/bin/env python3
"""Calcul du devis v1 de la course d'auto-conception (aucun appel) : tailles réelles des entrées (consigne du proposeur +
texte de chaque case, construit par la règle des lots du lanceur sur la matière v3 lue à son empreinte), nombre d'appels par
rôle, coûts estimés et hauts par espèce, part au pire par clé. Écrit `calcul-devis-course-auto-conception-v1.json` (refus
s'il existe déjà, R12).

Usage : python3 -I -B calcul-devis-course-auto-conception-v1.py MATIERE_V3.md
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
DEPOT = ICI.parents[2]
SORTIE = ICI / "calcul-devis-course-auto-conception-v1.json"

# Octets par jeton (texte français avec adresses) : estimation 3,3 ; borne haute 2,8 (plus de jetons).
OCTETS_PAR_JETON = {"estimation": 3.3, "haut": 2.8}
# Jetons de sortie par appel de proposeur (deux cartes ≈ 6 000 caractères, plus la réflexion) : estimation, haut.
SORTIE_PROPOSEUR = {"estimation": 6000, "haut": 16000}
# Prix en USD par million de jetons (entrée, sortie), avec leur source.
PRIX = {
    "prop-claude-1": ((4.0, 20.0), "barème du relais Claude de la procédure (`pole/relais_reel.py`, 1b90b020…, l. 49-54)"),
    "prop-claude-2": ((10.0, 50.0), "barème du relais Claude de la procédure (`pole/relais_reel.py`, 1b90b020…, l. 49-54)"),
    "prop-argon": ((8.3, 41.5), "prix figés de l'enveloppe d'Argon (`rapports/fille-ideation-1-v1/appel-argon-v5.sh`, 37c0205e…)"),
    "prop-kimi": ((2.0, 10.0), "procédure des relais persistants § 2.2 (prix vérifiés le 30 octobre, page `c62210a0…`)"),
    "prop-astra": ((10.0, 50.0), "`docs/notes/organisme-conception-propre-v1/prix-astra-v2.md` (bf211a07…), cité par la procédure § 2.2"),
    "prop-carbon": (None, "à relever (aucun prix lu ; espèce refusée tant que sa commande n'est pas épinglée)"),
}
# Coût par appel de l'aiguilleur et des juges : repris du devis v5 de la course d'affinage (entrées de même ordre :
# consigne de 2 à 4 ko plus une carte de 1 à 3 ko), `docs/notes/organisme-affinage-mentors-v1/devis-course-affinage-mentors-v5.md`
# (521470…) ; haut = 3 fois l'estimation.
PAR_APPEL_INTERNE = {"aiguilleur": 0.031, "juge-claude": 0.037, "juge-argon": 0.0347}
FACTEUR_HAUT_INTERNE = 3.0
CARTES = {"estimation": 2, "haut": 4}
PLAFONDS_SESSION = {"proposeur": 3.0, "aiguilleur": 0.25, "juge": 0.6}


def charger_lanceur():
    spec = importlib.util.spec_from_file_location("lanceur_auto_conception", DEPOT / "scripts" / "lancer_course_auto_conception_v1.py")
    m = importlib.util.module_from_spec(spec)
    sys.modules["lanceur_auto_conception"] = m
    spec.loader.exec_module(m)
    return m


def principal(argv: list) -> int:
    L = charger_lanceur()
    octets = Path(argv[0]).read_bytes()
    sha = hashlib.sha256(octets).hexdigest()
    if sha != L.MATIERE[1]:
        print(f"matière d'empreinte {sha}, {L.MATIERE[1]} épinglée", file=sys.stderr)
        return 2
    lots = L.decouper_matiere(octets, sha)
    consigne = (DEPOT / L.PIECES["consigne_proposeur"][0]).read_bytes()
    entrees = [len(consigne) + len(L.texte_de_case(lots, l).encode("utf-8")) + 200 for l in lots["lots"]]
    n_cases = len(entrees)
    especes = {}
    for e, ((pe, ps), _src) in ((k, v) for k, v in PRIX.items() if v[0] is not None):
        d = {}
        for regime in ("estimation", "haut"):
            jetons_e = sum(x / OCTETS_PAR_JETON[regime] for x in entrees)
            jetons_s = n_cases * SORTIE_PROPOSEUR[regime]
            d[regime] = round((jetons_e * pe + jetons_s * ps) / 1e6, 4)
        d["par_appel_estimation"] = round(d["estimation"] / n_cases, 4)
        d["par_appel_haut"] = round(d["haut"] / n_cases, 4)
        d["pire_par_appel_plafond_session"] = PLAFONDS_SESSION["proposeur"]
        especes[e] = d
    totaux = {}
    for extra in ([], ["prop-kimi"], ["prop-kimi", "prop-astra"]):
        actives = ["prop-claude-1", "prop-claude-2", "prop-argon"] + extra
        t = {}
        for regime in ("estimation", "haut"):
            cartes = n_cases * len(actives) * CARTES[regime]
            f = 1.0 if regime == "estimation" else FACTEUR_HAUT_INTERNE
            prop = sum(especes[e][regime] for e in actives)
            aig = cartes * PAR_APPEL_INTERNE["aiguilleur"] * f
            jug = cartes * (PAR_APPEL_INTERNE["juge-claude"] + PAR_APPEL_INTERNE["juge-argon"]) * f
            t[regime] = {"appels": {"proposeurs": n_cases * len(actives), "aiguilleur": cartes, "juges": 2 * cartes},
                         "cartes": cartes, "proposeurs_usd": round(prop, 4), "aiguilleur_usd": round(aig, 4),
                         "juges_usd": round(jug, 4), "total_usd": round(prop + aig + jug, 4)}
        totaux["+".join(sorted(actives))] = t
    sortie = {"version": "calcul-devis-course-auto-conception-v1", "matiere_sha256": sha, "cases": n_cases,
              "octets_entree_par_case": entrees, "octets_entree_total_par_espece": sum(entrees),
              "consigne_proposeur_octets": len(consigne), "hypotheses": {"octets_par_jeton": OCTETS_PAR_JETON,
              "sortie_proposeur_jetons": SORTIE_PROPOSEUR, "cartes_par_appel": CARTES, "par_appel_interne": PAR_APPEL_INTERNE,
              "facteur_haut_interne": FACTEUR_HAUT_INTERNE}, "prix": {k: {"usd_par_million": v[0], "source": v[1]} for k, v in PRIX.items()},
              "especes": especes, "totaux": totaux}
    with open(SORTIE, "x", encoding="utf-8") as f:
        f.write(json.dumps(sortie, ensure_ascii=False, indent=1) + "\n")
    print(json.dumps({"cases": n_cases, "especes": especes, "totaux": {k: {r: v[r]["total_usd"] for r in v} for k, v in totaux.items()}},
                     ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(principal(sys.argv[1:]))
