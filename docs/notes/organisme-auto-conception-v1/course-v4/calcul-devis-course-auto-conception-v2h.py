#!/usr/bin/env python3
"""Calcul du devis v2h — course d'auto-conception : Argon et Carbon proposeurs sans troncature, plafond par appel 6,05 USD.

Écrit le 19 novembre 2026 par le développeur unique de la version (modèle L′). Version neuve (R12 ; le calcul v2g reste en
place). Aucun appel, aucun réseau : lit des pièces scellées du dépôt (empreintes vérifiées), la matière dans
`refs/remotes/origin/main` (empreinte épinglée), calcule, écrit une sortie JSON scellée (compagnon `.sha256`). Bases : celles du
calcul v2g (coûts réels de la course v6 ; lots de Carbon de la v4 ; pensée de la v6 ; devis v2 pour l'aiguillage et les juges ;
épreuve v6), plus : Argon proposeur sans troncature (estimation : coût réel de la v6, faute de mesure sans budget de pensée ;
haut : la même pensée que Carbon en v6, 32 765 jetons, et 3 410 de réponse ; pire : la garde de la commande, aux deux comptes) ;
Argon juge (réglage v5 inchangé) : sortie que la garde retient sous 0,60 USD ; fonctions `controler_reglage_argon`,
`controler_reglage_carbon`, `pire_cas_sans_troncature` et `plus_grande_entree` du lanceur v8, chargées par leur chemin.

Usage (cwd = racine du dépôt) : python3 -I -B docs/notes/organisme-auto-conception-v1/course-v4/calcul-devis-course-auto-conception-v2h.py SORTIE.json
"""
import hashlib
import importlib.util
import json
import math
import sys
from pathlib import Path

VERSION = "calcul-devis-course-auto-conception-v2h"
DEPOT = Path(__file__).resolve().parents[4]
SOURCES = {
    "manifeste_fin_v6": ("runs/20261119-001004-course-auto-conception-v6/manifeste-lanceur-fin.json",
                         "3ed8cc610b33b8755488fc1a77bf889479b9e9b6c6fa7c5190200e8831183eaa"),
    "epreuve_v6": ("docs/notes/organisme-auto-conception-v1/course-v3/epreuve-temoins-reelle-auto-conception-v6.json",
                   "fe787c6291ead0d08703b37d59a35a2e7f98caf589cdf637695fe0ff69e02742"),
    "calcul_devis_v2": ("docs/notes/organisme-auto-conception-v1/calcul-devis-course-auto-conception-v2.json",
                        "91f5cf8f147689eb2fa9ff9db8b6e3b91b15496174e03f07a66d691676c2db2b"),
    "calcul_devis_v2g": ("docs/notes/organisme-auto-conception-v1/course-v4/calcul-devis-course-auto-conception-v2g.json",
                         "b01678ad8db9790fcef5f0ae5debb542f0ee5c36d772c5f8953f85bc1a821be5"),
    "configuration_v4": ("docs/notes/organisme-auto-conception-v1/course-v4/configuration-course-auto-conception-v4.json", None),
}
LANCEUR = DEPOT / "scripts" / "lancer_course_auto_conception_v8.py"
LOTS_CARBON_V4 = [(40986, 3410, 18823), (28791, 2202, 0), (34062, 3231, 17454), (29951, 3319, 20696)]   # diagnostic § 2
PENSEE_V6 = 32765
REPONSE_MAX_OBSERVEE = 3410
CASES = 11
PLAFOND_EPREUVE = 5.0
SONDE_ASTRA_MAX = 0.05
SONDE_CARBON_MAX = 6.0
CREDIT_MINUIT = 200.0
DEPENSE_ANTERIEURE_MINUIT = 0.000108
CLAUDE_EPREUVE = 0.972429          # dépense Claude de l'épreuve v6 (relevé des crédits v2e, champ « motif »)
PLAFOND_JUGE = 0.6


def sha256_fichier(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def lire(nom):
    rel, attendu = SOURCES[nom]
    p = DEPOT / rel
    h = sha256_fichier(p)
    compagnon = Path(str(p) + ".sha256")
    if attendu is not None and h != attendu:
        raise SystemExit(f"{rel} : empreinte {h}, {attendu} attendue")
    if not (compagnon.is_file() and compagnon.read_text(encoding="utf-8").split()[0] == h):
        raise SystemExit(f"{rel} : non scellé")
    return p, h


def charger_lanceur():
    spec = importlib.util.spec_from_file_location("lanceur_v8_pour_devis_v2h", LANCEUR)
    m = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = m
    spec.loader.exec_module(m)
    return m


def principal(argv):
    if len(argv) != 1:
        raise SystemExit("usage : calcul-devis-course-auto-conception-v2h.py SORTIE.json")
    sortie = Path(argv[0])
    if sortie.exists():
        raise SystemExit(f"{sortie} existe déjà (R12)")
    sources = {n: lire(n) for n in SOURCES}
    fin6 = json.loads(sources["manifeste_fin_v6"][0].read_text(encoding="utf-8"))
    ep6 = json.loads(sources["epreuve_v6"][0].read_text(encoding="utf-8"))
    dv2 = json.loads(sources["calcul_devis_v2"][0].read_text(encoding="utf-8"))["totaux"][
        "prop-argon+prop-astra+prop-carbon+prop-claude-1+prop-claude-2"]
    conf = json.loads(sources["configuration_v4"][0].read_text(encoding="utf-8"))
    L = charger_lanceur()
    pe, ps = L.PRIX_CARBON[0] / 1e6, L.PRIX_CARBON[1] / 1e6
    plafond_appel = float(conf["plafonds_session"]["proposeur"])

    octets, commit = L.lire_dans_main(DEPOT, L.MATIERE[0])
    if L.sha256_octets(octets) != L.MATIERE[1]:
        raise SystemExit("matière d'une autre empreinte")
    lots = L.decouper_matiere(octets, L.MATIERE[1])
    entree = L.plus_grande_entree((DEPOT / L.PIECES["consigne_proposeur"][0]).read_text(encoding="utf-8"), lots)
    pieces = {n: {"chemin": rel, "absolu": str(DEPOT / rel), "sha256": sha256_fichier(DEPOT / rel)}
              for n, (rel, _s) in L.PIECES.items() if (DEPOT / rel).is_file()}
    carbon = L.controler_reglage_carbon({"commande": ["bash", pieces["enveloppe_carbon"]["absolu"]],
                                         "modele_propose": L.MODELE_CARBON}, pieces, None)
    argon = L.controler_reglage_argon({"commande": ["bash", pieces["enveloppe_argon_sans_troncature"]["absolu"]]}, pieces)
    pire_c = L.pire_cas_sans_troncature(carbon, entree, plafond_appel, "Carbon")
    pire_a = L.pire_cas_sans_troncature(argon, entree, plafond_appel, "Argon proposeur")

    # Argon juge (réglage v5) : sortie retenue par la garde sous 0,60 USD, consigne de juge et fiche de 9 000 caractères
    j = argon["juge"]
    cj = len((DEPOT / L.PIECES["consigne_juge"][0]).read_text(encoding="utf-8"))
    juge = {}
    for fiche in (3000, 9000):
        chars = cj + fiche + 300
        e = math.ceil(math.ceil(chars / j["caracteres_par_jeton"]) * (1 + j["marge_entree"]))
        place = math.floor((PLAFOND_JUGE - e * pe) / ps)
        juge[f"fiche_{fiche}_caracteres"] = {"entree_gardee": e, "max_output_tokens": min(j["max_sortie_jetons"],
                                                                                           place - j["provision_pensee_jetons"]),
                                             "thinking_budget": j["provision_pensee_jetons"],
                                             "sans_troncature_sortie_egale_provision_au_plus": math.floor((PLAFOND_JUGE - e * pe) / (2 * ps))}

    couts_v4 = [e * pe + (s + p) * ps for e, s, p in LOTS_CARBON_V4]
    carbon_estime = sum(couts_v4) / len(couts_v4)
    haut_appel = max(e for e, _s, _p in LOTS_CARBON_V4) * pe + (PENSEE_V6 + REPONSE_MAX_OBSERVEE) * ps
    par_role6 = fin6["cout_reel"]["par_role_usd"]
    autres = {r: par_role6[r] for r in ("prop-opus", "prop-fable", "prop-astra")}
    prop_est = dict(autres, **{"prop-argon": par_role6["prop-argon"], "prop-carbon": round(CASES * carbon_estime, 6)})
    proposition_est = round(sum(prop_est.values()), 6)
    proposition_haut = round(sum(autres.values()) + 2 * CASES * haut_appel, 6)
    pire_appel = pire_c["pire_cas_usd"]
    aig_est, jug_est = dv2["estimation"]["aiguilleur_usd"], dv2["estimation"]["juges_usd"]
    aig_haut, jug_haut = dv2["haut"]["aiguilleur_usd"], dv2["haut"]["juges_usd"]
    course_est = round(proposition_est + aig_est + jug_est, 6)
    course_haut = round(proposition_haut + aig_haut + jug_haut, 6)

    b = conf["budget"]
    s17 = float(b["plafond_usd"])
    et = {e["nom"]: e for e in b["etapes"]}
    att = {n: float(et[n]["attendu_usd"]) for n in et}
    rel = {n: float(et[n]["plafond_relais_usd"]) for n in et}
    dur_proposition = max(rel["proposition"], s17 - (att["aiguillage"] + att["juges"]))
    seuil_aig, seuil_juges = s17 - rel["aiguillage"], s17 - rel["juges"]

    def lecture(cumul_prop, aig):
        cumul_prop = min(cumul_prop, dur_proposition)
        lance_aig = cumul_prop <= seuil_aig + 1e-9
        dur_aig = max(rel["aiguillage"], s17 - cumul_prop - att["juges"])
        cumul_av = cumul_prop + (min(aig, dur_aig) if lance_aig else 0.0)
        return {"cumul_apres_proposition_usd": round(cumul_prop, 6), "aiguillage_lance": lance_aig,
                "plafond_dur_aiguillage_usd": round(dur_aig, 2), "cumul_avant_juges_usd": round(cumul_av, 6),
                "juges_lances": lance_aig and cumul_av <= seuil_juges + 1e-9, "plafond_dur_juges_usd": round(max(rel["juges"], s17 - cumul_av), 2)}

    base_sans_ac = sum(autres.values())
    epreuve_est = float(ep6["cout_usd"])
    sonde_carbon_est = round(math.ceil(entree["caracteres"] / 3.0) * pe + (PENSEE_V6 + REPONSE_MAX_OBSERVEE) * ps, 6)
    total_est = round(course_est + epreuve_est + sonde_carbon_est + SONDE_ASTRA_MAX, 6)
    reste_net = round(CREDIT_MINUIT - DEPENSE_ANTERIEURE_MINUIT - CLAUDE_EPREUVE, 6)
    # au-delà de quelle dépense d'Argon et de Carbon proposeurs (ensemble, onze appels chacun) les juges ne sont plus lancés
    marge_ac_estimation = round(seuil_juges - base_sans_ac - aig_est, 6)
    marge_ac_haut = round(seuil_juges - base_sans_ac - aig_haut, 6)

    out = {
        "version": VERSION, "commit_main": commit,
        "sources": {n: {"chemin": SOURCES[n][0], "sha256": h} for n, (_p, h) in sources.items()},
        "lanceur_v8": {"chemin": str(LANCEUR.relative_to(DEPOT)), "sha256": sha256_fichier(LANCEUR)},
        "plafond_session_proposeur_usd": plafond_appel,
        "plus_grande_entree": {k: entree[k] for k in ("rang", "nom", "octets", "caracteres", "sha256")},
        "carbon": {"reglage": carbon["valeurs"], "drapeaux": carbon["drapeaux"], "pire_cas_appel": pire_c,
                   "estimation_par_appel_usd": round(carbon_estime, 6), "haut_par_appel_usd": round(haut_appel, 6),
                   "onze_appels": {"estimation_usd": round(CASES * carbon_estime, 6), "haut_usd": round(CASES * haut_appel, 6),
                                   "pire_usd": round(CASES * pire_appel, 6)}},
        "argon_proposeur": {"reglage": argon["valeurs"], "drapeaux": argon["drapeaux"], "pire_cas_appel": pire_a,
                            "reglage_v5_remplace": {"delai_s": 1500.0, "provision_et_thinking_budget": 8192, "caracteres_par_jeton": 4.0,
                                                    "sortie_retenue_sous_3_usd": 57265, "timeout": [20, 1700]},
                            "estimation_par_appel_usd": round(par_role6["prop-argon"] / CASES, 6),
                            "haut_par_appel_usd": round(haut_appel, 6),
                            "onze_appels": {"estimation_usd": par_role6["prop-argon"], "haut_usd": round(CASES * haut_appel, 6),
                                            "pire_usd": round(CASES * pire_a["pire_cas_usd"], 6)}},
        "argon_juge": {"reglage": j, "plafond_session_usd": PLAFOND_JUGE, **juge},
        "proposition": {"estimation_par_role_usd": prop_est, "estimation_usd": proposition_est, "haut_usd": proposition_haut,
                        "plafond_dur_au_lancement_usd": round(dur_proposition, 2)},
        "aiguillage": {"estimation_usd": aig_est, "haut_usd": aig_haut},
        "juges": {"estimation_usd": jug_est, "haut_usd": jug_haut},
        "seuils_internes": {"s17_usd": s17, "aiguillage_lance_si_cumul_au_plus_usd": seuil_aig,
                            "juges_lances_si_cumul_au_plus_usd": seuil_juges,
                            "a_l_estimation": lecture(proposition_est, aig_est), "au_haut": lecture(proposition_haut, aig_haut),
                            "carbon_au_pire": lecture(base_sans_ac + par_role6["prop-argon"] + CASES * pire_appel, aig_haut),
                            "argon_et_carbon_au_pire": lecture(base_sans_ac + 2 * CASES * pire_appel, aig_haut),
                            "argon_et_carbon_ensemble_au_plus_pour_lancer_les_juges_usd": {
                                "aiguillage_estime": marge_ac_estimation, "aiguillage_haut": marge_ac_haut}},
        "course": {"estimation_usd": course_est, "haut_usd": course_haut, "plafond_arret_usd": s17},
        "epreuve_v8": {"estimation_usd": epreuve_est, "plafond_usd": PLAFOND_EPREUVE},
        "sonde_carbon": {"estimation_usd": sonde_carbon_est, "plafond_usd": SONDE_CARBON_MAX},
        "sonde_astra": {"au_plus_usd": SONDE_ASTRA_MAX},
        "total": {"estimation_usd": total_est, "au_pire_usd": round(s17 + PLAFOND_EPREUVE + SONDE_CARBON_MAX + SONDE_ASTRA_MAX, 6)},
        "parts_au_pire_par_cle_usd": {"claude (Minuit)": s17, "gemini (Argon : juge ; Carbon 11 × 6,05)": s17,
                                      "openai (Astra : 11 × 6,05)": round(min(CASES * plafond_appel, s17), 6)},
        "relais_argon": {"appels_d_argon_au_pire": 231, "borne_relais_exigee": L.appels_relais_gemini_requis(231)},
        "cle_claude": {"variable": "RR_ANTHROPIC_API_KEY_MINUIT", "credit_declare_usd": CREDIT_MINUIT,
                       "depense_anterieure_inscrite_usd": DEPENSE_ANTERIEURE_MINUIT, "epreuve_claude_estimee_usd": CLAUDE_EPREUVE,
                       "reserves_usd": 0.0, "reste_net_estime_au_depart_usd": reste_net, "part_au_pire_usd": s17,
                       "depart_admis": reste_net > s17 and reste_net >= CREDIT_MINUIT / 5,
                       "reste_estime_apres_course_au_pire_usd": round(reste_net - s17, 6)},
    }
    sortie.parent.mkdir(parents=True, exist_ok=True)
    donnees = (json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True) + "\n").encode("utf-8")
    with open(sortie, "xb") as f:
        f.write(donnees)
    h = hashlib.sha256(donnees).hexdigest()
    with open(str(sortie) + ".sha256", "x", encoding="utf-8") as f:
        f.write(f"{h}  {sortie.name}\n")
    print(json.dumps({"sortie": str(sortie), "sha256": h, "total": out["total"], "course": out["course"],
                      "proposition": out["proposition"], "carbon": out["carbon"]["onze_appels"],
                      "argon": out["argon_proposeur"]["onze_appels"], "pires": [pire_c["pire_cas_usd"], pire_a["pire_cas_usd"]],
                      "juge": juge, "seuils": out["seuils_internes"], "cle": out["cle_claude"], "relais": out["relais_argon"]},
                     ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
