#!/usr/bin/env python3
"""Calcul du devis v2g — course d'auto-conception, Carbon par la commande synchrone d'Argon, sans troncature, plafonds relevés.

Écrit le 19 novembre 2026 par le développeur unique de la version (modèle L′). Aucun appel, aucun réseau : lit des pièces
scellées du dépôt (empreintes vérifiées), la matière dans `refs/remotes/origin/main` (empreinte épinglée), calcule, écrit une
sortie JSON scellée (compagnon `.sha256`). Bases :
- coûts **réels** de la course v6 (manifeste de fin `3ed8cc61…`) pour Opus, Fable, Argon et Astra (onze appels chacun) ;
- Carbon : usage des quatre lots de la course v4 (diagnostic `510312b1…`, § 2, transcrit) pour l'estimation ; pour le haut,
  la pensée qui a rempli la sortie en v6 (32 765 jetons, journal provisoire v62, PO-178, `532f9245…`, transcrit) plus la
  réponse la plus longue observée (3 410) sur la plus grande entrée gardée ; le pire cas d'un appel par la garde de la commande
  (fonctions `pire_cas_carbon` et `plus_grande_entree` du lanceur v7, chargées par leur chemin) ;
- aiguillage et juges : calcul du devis v2 (`91f5cf8f…`, composition déclarée) ; épreuve : coût réel de l'épreuve v6
  (`fe787c62…`) ;
- règle d'A1 de l'orchestrateur (`pole/budget_v56.py`) pour les plafonds d'étape : plafond dur d'une étape protégée = max(son
  plafond de relais ; S17 − cumul − attendus des étapes restantes) ; une étape protégée n'est lancée que si cumul + son plafond
  de relais ≤ S17.

Usage (cwd = racine du dépôt) : python3 -I -B docs/notes/organisme-auto-conception-v1/course-v4/calcul-devis-course-auto-conception-v2g.py SORTIE.json
"""
import hashlib
import importlib.util
import json
import math
import sys
from pathlib import Path

VERSION = "calcul-devis-course-auto-conception-v2g"
DEPOT = Path(__file__).resolve().parents[4]
SOURCES = {
    "manifeste_fin_v6": ("runs/20261119-001004-course-auto-conception-v6/manifeste-lanceur-fin.json",
                         "3ed8cc610b33b8755488fc1a77bf889479b9e9b6c6fa7c5190200e8831183eaa"),
    "manifeste_fin_v4": ("runs/20261118-171908-course-auto-conception-v4/manifeste-lanceur-fin.json",
                         "2625234c786a7fc50c926325c1a9efc8a8e9b74146a59205bf8a31c6e2c5fd7f"),
    "epreuve_v6": ("docs/notes/organisme-auto-conception-v1/course-v3/epreuve-temoins-reelle-auto-conception-v6.json",
                   "fe787c6291ead0d08703b37d59a35a2e7f98caf589cdf637695fe0ff69e02742"),
    "calcul_devis_v2": ("docs/notes/organisme-auto-conception-v1/calcul-devis-course-auto-conception-v2.json",
                        "91f5cf8f147689eb2fa9ff9db8b6e3b91b15496174e03f07a66d691676c2db2b"),
    "diagnostic": ("docs/notes/organisme-auto-conception-v1/course-v2/diagnostic-erreurs-carbon-astra-course-v4-v1.md",
                   "510312b105c62ad01a1d45ab9078dfc04333ce3bc2322b98695fa48c4daa8aec"),
    "journal_v62": ("registres-provisoires/compte-organisme-2026-11-19-v62.md",
                    "532f92457628b9401d17e745e4a9f64c6bb80208ec85534c9b8d30236e7d94f0"),
    "configuration_v3": ("docs/notes/organisme-auto-conception-v1/course-v4/configuration-course-auto-conception-v3.json", None),
}
LANCEUR = DEPOT / "scripts" / "lancer_course_auto_conception_v7.py"
LOTS_CARBON_V4 = [(40986, 3410, 18823), (28791, 2202, 0), (34062, 3231, 17454), (29951, 3319, 20696)]   # diagnostic § 2
PENSEE_V6 = 32765          # journal v62, PO-178 : la pensée a rempli la sortie de 32 768 aux trois lots
REPONSE_MAX_OBSERVEE = 3410
CASES = 11
PLAFOND_EPREUVE = 5.0
SONDE_ASTRA_MAX = 0.05
SONDE_CARBON_MAX = 6.0
CREDIT_MINUIT = 200.0              # R-3228, mère R-3616
DEPENSE_ANTERIEURE_MINUIT = 0.000108   # appel minimal de vérification du 19 novembre à 06:37:04Z (mère R-3616)


def sha256_fichier(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def lire(nom):
    rel, attendu = SOURCES[nom]
    p = DEPOT / rel
    h = sha256_fichier(p)
    compagnon = Path(str(p) + ".sha256")
    scelle = compagnon.is_file() and compagnon.read_text(encoding="utf-8").split()[0] == h
    if attendu is not None and h != attendu:
        raise SystemExit(f"{rel} : empreinte {h}, {attendu} attendue")
    if not scelle:
        raise SystemExit(f"{rel} : non scellé")
    return p, h


def charger_lanceur():
    spec = importlib.util.spec_from_file_location("lanceur_v7_pour_devis_v2g", LANCEUR)
    m = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = m
    spec.loader.exec_module(m)
    return m


def principal(argv):
    if len(argv) != 1:
        raise SystemExit("usage : calcul-devis-course-auto-conception-v2g.py SORTIE.json")
    sortie = Path(argv[0])
    if sortie.exists():
        raise SystemExit(f"{sortie} existe déjà (R12)")
    sources = {n: lire(n) for n in SOURCES}
    fin6 = json.loads(sources["manifeste_fin_v6"][0].read_text(encoding="utf-8"))
    fin4 = json.loads(sources["manifeste_fin_v4"][0].read_text(encoding="utf-8"))
    ep6 = json.loads(sources["epreuve_v6"][0].read_text(encoding="utf-8"))
    dv2 = json.loads(sources["calcul_devis_v2"][0].read_text(encoding="utf-8"))["totaux"][
        "prop-argon+prop-astra+prop-carbon+prop-claude-1+prop-claude-2"]
    conf = json.loads(sources["configuration_v3"][0].read_text(encoding="utf-8"))
    L = charger_lanceur()
    pe, ps = L.PRIX_CARBON[0] / 1e6, L.PRIX_CARBON[1] / 1e6

    # --- Carbon : pire cas d'un appel sur la plus grande entrée servie, par la garde de la commande ---
    octets, commit = L.lire_dans_main(DEPOT, L.MATIERE[0])
    if L.sha256_octets(octets) != L.MATIERE[1]:
        raise SystemExit("matière d'une autre empreinte")
    lots = L.decouper_matiere(octets, L.MATIERE[1])
    consigne = (DEPOT / L.PIECES["consigne_proposeur"][0]).read_text(encoding="utf-8")
    entree = L.plus_grande_entree(consigne, lots)
    pieces = {n: {"chemin": rel, "absolu": str(DEPOT / rel), "sha256": sha256_fichier(DEPOT / rel)}
              for n, (rel, _s) in L.PIECES.items() if (DEPOT / rel).is_file()}
    reglage = L.controler_reglage_carbon({"commande": ["bash", pieces["enveloppe_carbon"]["absolu"]],
                                          "modele_propose": L.MODELE_CARBON}, pieces, None)
    plafond_appel = float(conf["plafonds_session"]["proposeur"])
    pire = L.pire_cas_carbon(reglage, entree, plafond_appel)
    pire_appel = pire["pire_cas_usd"]

    couts_v4 = [e * pe + (s + p) * ps for e, s, p in LOTS_CARBON_V4]
    carbon_estime = sum(couts_v4) / len(couts_v4)
    entree_reelle_max = max(e for e, _s, _p in LOTS_CARBON_V4)
    carbon_haut = entree_reelle_max * pe + (PENSEE_V6 + REPONSE_MAX_OBSERVEE) * ps

    par_role6 = fin6["cout_reel"]["par_role_usd"]
    prop_base = {r: par_role6[r] for r in ("prop-opus", "prop-fable", "prop-argon", "prop-astra")}
    prop_est = dict(prop_base, **{"prop-carbon": round(CASES * carbon_estime, 6)})
    proposition_est = round(sum(prop_est.values()), 6)
    proposition_haut = round(sum(prop_base.values()) + CASES * carbon_haut, 6)
    proposition_pire_carbon = round(sum(prop_base.values()) + CASES * pire_appel, 6)
    aig_est, jug_est = dv2["estimation"]["aiguilleur_usd"], dv2["estimation"]["juges_usd"]
    aig_haut, jug_haut = dv2["haut"]["aiguilleur_usd"], dv2["haut"]["juges_usd"]
    course_est = round(proposition_est + aig_est + jug_est, 6)
    course_haut = round(proposition_haut + aig_haut + jug_haut, 6)

    # --- plafonds d'étape (règle d'A1), seuils internes ---
    b = conf["budget"]
    s17 = float(b["plafond_usd"])
    et = {e["nom"]: e for e in b["etapes"]}
    att = {n: float(et[n]["attendu_usd"]) for n in et}
    rel = {n: float(et[n]["plafond_relais_usd"]) for n in et}
    dur_proposition = max(rel["proposition"], s17 - 0.0 - (att["aiguillage"] + att["juges"]))
    seuil_aiguillage = s17 - rel["aiguillage"]      # cumul au plus pour lancer l'aiguillage
    seuil_juges = s17 - rel["juges"]                # cumul au plus pour lancer les juges

    def lecture(cumul_prop, aig):
        """Cumul après la proposition → l'aiguillage est-il lancé, à quel plafond dur ; son coût (borné par ce plafond dur) →
        les juges sont-ils lancés, à quel plafond dur."""
        lance_aig = cumul_prop <= seuil_aiguillage + 1e-9
        dur_aig = max(rel["aiguillage"], s17 - cumul_prop - att["juges"])
        cumul_av_juges = cumul_prop + (min(aig, dur_aig) if lance_aig else 0.0)
        return {"cumul_apres_proposition_usd": round(cumul_prop, 6), "aiguillage_lance": lance_aig,
                "plafond_dur_aiguillage_usd": round(dur_aig, 2),
                "cumul_avant_juges_usd": round(cumul_av_juges, 6), "juges_lances": lance_aig and cumul_av_juges <= seuil_juges + 1e-9,
                "plafond_dur_juges_usd": round(max(rel["juges"], s17 - cumul_av_juges), 2)}

    epreuve_est = float(ep6["cout_usd"])
    sonde_carbon_est = round(entree["caracteres"] / 3.0 * pe + (PENSEE_V6 + REPONSE_MAX_OBSERVEE) * ps, 6)
    total_est = round(course_est + epreuve_est + sonde_carbon_est + SONDE_ASTRA_MAX, 6)

    # --- parts au pire par clé (règle du lanceur : relais qui tient l'aiguilleur ou un juge → plafond d'arrêt) ---
    parts = {"claude (Minuit)": s17, "gemini (Argon : juge ; Carbon : 11 × 6)": s17,
             "openai (Astra : 11 × 6)": round(min(CASES * plafond_appel, s17), 6)}
    claude_epreuve = 0.972429      # dépense Claude de l'épreuve v6 lue au relais 8787 (relevé des crédits v2e, champ « motif »)
    reste_net = round(CREDIT_MINUIT - DEPENSE_ANTERIEURE_MINUIT - claude_epreuve, 6)

    out = {
        "version": VERSION, "commit_main": commit,
        "sources": {n: {"chemin": SOURCES[n][0], "sha256": h} for n, (_p, h) in sources.items()},
        "lanceur_v7": {"chemin": str(LANCEUR.relative_to(DEPOT)), "sha256": sha256_fichier(LANCEUR)},
        "base_v6": {"par_role_usd": par_role6, "appels_par_role": fin6["cout_reel"]["appels_par_role"],
                    "total_usd": fin6["cout_reel"]["total_usd"], "etapes": fin6["ce_qui_a_ete_fait"]["etapes"]},
        "base_v4_total_usd": fin4["cout_reel"]["total_usd"],
        "carbon": {"reglage": reglage["valeurs"], "drapeaux": reglage["drapeaux"],
                   "plus_grande_entree": {k: entree[k] for k in ("rang", "nom", "octets", "caracteres", "sha256")},
                   "pire_cas_appel": pire, "estimation_par_appel_usd": round(carbon_estime, 6),
                   "haut_par_appel_usd": round(carbon_haut, 6), "lots_v4": LOTS_CARBON_V4, "pensee_v6_jetons": PENSEE_V6,
                   "onze_appels": {"estimation_usd": round(CASES * carbon_estime, 6), "haut_usd": round(CASES * carbon_haut, 6),
                                   "pire_usd": round(CASES * pire_appel, 6)}},
        "proposition": {"estimation_par_role_usd": prop_est, "estimation_usd": proposition_est, "haut_usd": proposition_haut,
                        "pire_carbon_compris_usd": proposition_pire_carbon,
                        "plafond_dur_au_lancement_usd": round(dur_proposition, 2)},
        "aiguillage": {"estimation_usd": aig_est, "haut_usd": aig_haut},
        "juges": {"estimation_usd": jug_est, "haut_usd": jug_haut},
        "seuils_internes": {"s17_usd": s17, "aiguillage_lance_si_cumul_au_plus_usd": seuil_aiguillage,
                            "juges_lances_si_cumul_au_plus_usd": seuil_juges,
                            "a_l_estimation": lecture(proposition_est, aig_est), "au_haut": lecture(proposition_haut, aig_haut),
                            "carbon_au_pire_autres_au_reel_v6": lecture(proposition_pire_carbon, aig_haut),
                            "proposition_au_plafond_dur": lecture(dur_proposition, aig_haut)},
        "course": {"estimation_usd": course_est, "haut_usd": course_haut, "plafond_arret_usd": s17},
        "epreuve_v7": {"estimation_usd": epreuve_est, "plafond_usd": PLAFOND_EPREUVE},
        "sonde_carbon": {"estimation_usd": sonde_carbon_est, "plafond_usd": SONDE_CARBON_MAX,
                         "pire_usd": pire_appel},
        "sonde_astra": {"au_plus_usd": SONDE_ASTRA_MAX},
        "total": {"estimation_usd": total_est, "au_pire_usd": round(s17 + PLAFOND_EPREUVE + SONDE_CARBON_MAX + SONDE_ASTRA_MAX, 6)},
        "parts_au_pire_par_cle_usd": parts,
        "cle_claude": {"variable": "RR_ANTHROPIC_API_KEY_MINUIT", "credit_declare_usd": CREDIT_MINUIT,
                       "depense_anterieure_inscrite_usd": DEPENSE_ANTERIEURE_MINUIT,
                       "epreuve_v7_claude_estimee_usd": claude_epreuve, "reserves_usd": 0.0,
                       "reste_net_estime_au_depart_usd": reste_net, "part_au_pire_usd": s17,
                       "depart_admis": reste_net > s17 and reste_net >= CREDIT_MINUIT / 5,
                       "reste_estime_apres_course_au_pire_usd": round(reste_net - s17, 6),
                       "part_claude_de_la_course_v6_usd": fin6["cout_reel"]["par_relais_usd"]["claude"]},
    }
    sortie.parent.mkdir(parents=True, exist_ok=True)
    donnees = (json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True) + "\n").encode("utf-8")
    with open(sortie, "xb") as f:
        f.write(donnees)
    h = hashlib.sha256(donnees).hexdigest()
    with open(str(sortie) + ".sha256", "x", encoding="utf-8") as f:
        f.write(f"{h}  {sortie.name}\n")
    print(json.dumps({"sortie": str(sortie), "sha256": h, "total": out["total"], "course": out["course"],
                      "carbon": out["carbon"]["onze_appels"], "pire_appel": pire_appel, "seuils": out["seuils_internes"],
                      "cle_claude": out["cle_claude"]}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
