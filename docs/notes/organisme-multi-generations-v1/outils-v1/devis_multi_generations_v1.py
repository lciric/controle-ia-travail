"""Devis estimé : (a) écriture du monde riche par Kimi ; (b) course de l'organisme à plusieurs générations — v1.

Concepteur neuf (Claude Opus 5.5), 12 novembre 2026. Bibliothèque standard seule ; aucun appel. Chaque hypothèse est écrite
ci-dessous avec sa source (chemin et empreinte abrégée) ou marquée « estimé ». Usage : `python3 -I -B
devis_multi_generations_v1.py SORTIE.json` (refuse d'écraser).
"""

import json
import os
import sys

PRIX = {  # USD par million de jetons (entrée, sortie)
    "kimi-k3.1-pro": (2.0, 10.0, "docs/notes/ideation-organisme-v1/relais-kimi-v1/LISEZMOI-relais-kimi-v4.md l. 57-58 (e5d6c5ce…), page des prix lue le 30 octobre"),
    "claude-opus-5-5": (4.0, 20.0, "docs/notes/credits-claude-v1/plan-chiffre-credits-claude-v1.md section 1 (8f9ee89e…), « à relire avant chaque devis »"),
    "claude-fable-5-2": (8.0, 40.0, "même source"),
    "claude-fable-5-1": (10.0, 50.0, "même source"),
    "gemini-4-argon": (10.0, 50.0, "commande_argon_v56_nuit_v6.py PRIX l. 234 (5eae1a04…), « prix prudent (SUPPOSÉ) »"),
    "gpt-6-astra": (10.0, 50.0, "collisionneur_v8.py l. 79-82 (22e5ed8a…), « Prix SUPPOSÉS »"),
}


def cout(modele, e, s):
    pe, ps, _ = PRIX[modele]
    return (e * pe + s * ps) / 1e6


def monde_par_kimi(mondes):
    # un appel : consigne ≈ 4 000 jetons (estimé : ≈ 9 Ko de texte) ; sortie centrale 35 000 (estimé d'après les deux appels
    # du proposeur Kimi de la course v67 : 31 891 et 38 343 jetons, verdict v67 section 4.1, d7902432…) ; pire cas : borne
    # de sortie de la configuration v8, 131 072 jetons (texte v2, écart 1, 80fe4f03…).
    central = cout("kimi-k3.1-pro", 4000, 35000)
    pire = cout("kimi-k3.1-pro", 6000, 131072)
    appels_pire = 3 * mondes  # un appel, puis au plus deux corrections ou reprises par monde (estimé)
    return {"mondes": mondes, "appel_central_usd": round(central, 3), "appel_pire_usd": round(pire, 3),
            "appels_attendus": mondes, "appels_pire": appels_pire,
            "attendu_usd": round(central * mondes, 2), "pire_usd": round(pire * appels_pire, 2)}


# Course : par monde et par génération.
PROPOSEURS_CENTRAL = {  # USD par appel, estimé
    "claude-opus-5-5": cout("claude-opus-5-5", 25000, 35000),     # entrée 25 000 (estimé : consigne, vue, épisodes), sortie 35 000
    "claude-fable-5-2": cout("claude-fable-5-2", 25000, 35000),
    "gemini-4-argon": 0.25,  # estimé : coût total d'Argon en v67 (0,85618 USD, 16 appels dont 14 de vérificateur, verdict v67 § 4.5)
    "gpt-6-astra": cout("gpt-6-astra", 25000, 15000),            # estimé : sortie 15 000 (aucune mesure sur ce rôle)
}
PLAFOND_SESSION_PROPOSEUR = 2.0  # USD, garde proposée (la v8 avait 1,50 pour Kimi) : pire cas par appel de proposeur
TEST_CENTRAL = {"kimi-k3.1-pro": 2 * 0.02 + 0.06,   # devis v66, section 3.3 (60643868…) : 2 tours à 0,02, vérificateur 0,06
                "claude-opus-5-5": 2 * cout("claude-opus-5-5", 8000, 2000) + 0.06,  # estimé : tour 8 000 / 2 000 jetons
                "gemini-4-argon": 2 * cout("gemini-4-argon", 8000, 2000) + 0.06}
TEST_PIRE = 0.80 + 0.10  # borne par carte de l'expérimentateur (12 tours) et du vérificateur, devis v66 section 3.4


def course(mondes, generations, experimentateur, tests_central=15, tests_pire=33):
    """tests : représentants promus (central 6, pire 24) + vraies plantées et T-ELIM promues (central 9, pire 9) ; les
    fausses et les copies promues ne sont pas testées (brèche lue à la promotion) : estimé."""
    par_gen_central = {m: c for m, c in PROPOSEURS_CENTRAL.items()}
    t_c = TEST_CENTRAL[experimentateur]
    lignes = {}
    for f in ("claude", "argon", "astra", "kimi"):
        lignes[f] = {"central": 0.0, "pire": 0.0}
    lignes["claude"]["central"] += par_gen_central["claude-opus-5-5"] + par_gen_central["claude-fable-5-2"]
    lignes["claude"]["pire"] += 2 * PLAFOND_SESSION_PROPOSEUR
    lignes["argon"]["central"] += par_gen_central["gemini-4-argon"]
    lignes["argon"]["pire"] += PLAFOND_SESSION_PROPOSEUR
    lignes["astra"]["central"] += par_gen_central["gpt-6-astra"]
    lignes["astra"]["pire"] += PLAFOND_SESSION_PROPOSEUR
    exp = {"kimi-k3.1-pro": "kimi", "claude-opus-5-5": "claude", "gemini-4-argon": "argon"}[experimentateur]
    lignes[exp]["central"] += tests_central * (t_c - 0.06)
    lignes[exp]["pire"] += tests_pire * 0.80
    lignes["argon"]["central"] += tests_central * 0.06          # vérificateur Argon (autre famille)
    lignes["argon"]["pire"] += tests_pire * 0.10
    k = mondes * generations
    out = {f: {"central_usd": round(v["central"] * k, 2), "pire_usd": round(v["pire"] * k, 2)} for f, v in lignes.items()}
    out["total_modeles"] = {"central_usd": round(sum(v["central"] for v in lignes.values()) * k, 2),
                            "pire_usd": round(sum(v["pire"] for v in lignes.values()) * k, 2)}
    out["machine"] = {"central_usd": round(0.15 * k, 2), "plafond_usd": 10.0,
                      "base": "course v67 : ≈ 2 heures, ≈ 0,12 EUR (verdict v67 § 4.5) ; ≈ 1 à 2 heures par génération et par monde (estimé)"}
    out["parametres"] = {"mondes": mondes, "generations": generations, "experimentateur": experimentateur,
                         "tests_par_generation": {"central": tests_central, "pire": tests_pire}}
    return out


def main(argv):
    if len(argv) != 2 or os.path.exists(argv[1]):
        print("usage : devis_multi_generations_v1.py SORTIE.json (neuf)")
        return 2
    res = {"prix": {k: {"entree": v[0], "sortie": v[1], "source": v[2]} for k, v in PRIX.items()},
           "proposeurs_central_par_appel_usd": {k: round(v, 3) for k, v in PROPOSEURS_CENTRAL.items()},
           "test_central_usd": {k: round(v, 3) for k, v in TEST_CENTRAL.items()}, "test_pire_usd": TEST_PIRE,
           "monde_par_kimi": {str(m): monde_par_kimi(m) for m in (1, 2, 3)},
           "course": {f"{m}-mondes|{g}-generations|exp={e}": course(m, g, e)
                      for m in (1, 2, 3) for g in (3, 4) for e in ("claude-opus-5-5", "kimi-k3.1-pro", "gemini-4-argon")}}
    with open(argv[1], "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1, sort_keys=True)
    for cle in ("1-mondes|3-generations|exp=claude-opus-5-5", "2-mondes|3-generations|exp=claude-opus-5-5",
                "3-mondes|3-generations|exp=claude-opus-5-5", "2-mondes|3-generations|exp=kimi-k3.1-pro"):
        print(cle, json.dumps(res["course"][cle], ensure_ascii=False))
    print("monde par Kimi", json.dumps(res["monde_par_kimi"], ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
