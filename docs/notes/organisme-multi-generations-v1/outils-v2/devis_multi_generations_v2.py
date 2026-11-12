"""Devis v2 de la course à plusieurs générations, pire cas **par formule** (correction E-9 de la contre-lecture `e7d5cda0…`) ;
plafonds de session par modèle (S-6). Bibliothèque standard ; aucun appel. Usage : `python3 -I -B devis_multi_generations_v2.py SORTIE.json`.

Par monde et par génération :
  pire = Σ plafonds de session des proposeurs + T_pire × (borne par test de l'expérimentateur + borne du vérificateur)
  T_pire = représentants (au plus une carte sur une : 6 × proposeurs) + vraies plantées **replantées à chaque génération**
           (le monde, au plus 9 « K1 + un effet », 2 diluées, T-ELIM : 13) [+ 8 si les fausses et copies promues sont testées]
  central = Σ appels centraux + T_central × (coût central d'un test), T_central = 6 représentants + 10 plantées promues.
Hypothèses chiffrées : prix du plan des crédits (`8f9ee89e…`), de Kimi (`e5d6c5ce…`), supposés pour Argon et Astra ; tour
d'expérimentateur au pire 8 000 jetons d'entrée et 4 000 de sortie (estimé), 12 tours au plus ; borne par test = 12 tours
arrondis au-dessus ; un test coupé par sa borne est « non concluant » (le groupe est éliminé, rapporté).
"""
import json
import os
import sys

PRIX = {"opus": (4.0, 20.0), "fable52": (8.0, 40.0), "argon": (10.0, 50.0), "astra": (10.0, 50.0), "kimi": (2.0, 10.0)}
PLAFOND_SESSION = {"opus": 2.0, "fable52": 3.0, "argon": 2.0, "astra": 2.0, "kimi": 1.5}  # S-6 : Fable 5.2 à 3 USD ≈ 75 000 jetons de sortie
CENTRAL_PROPOSEUR = {"opus": 0.80, "fable52": 1.60, "argon": 0.25, "astra": 1.00, "kimi": 0.36}  # devis v1 (estimé)
BORNE_TEST = {"opus": 1.50, "kimi": 0.80, "argon": 3.40}  # 12 × (8 000 × entrée + 4 000 × sortie), arrondi ; Kimi : devis v66
CENTRAL_TOUR = {m: (8000 * PRIX[m][0] + 2000 * PRIX[m][1]) / 1e6 for m in ("opus", "kimi", "argon")}
VERIF_CENTRAL, VERIF_PIRE = 0.06, 0.10  # vérificateur Argon, devis v66
PLANTEES_PIRE, PLANTEES_CENTRAL, FAUSSES_ET_COPIES = 13, 10, 8


def course(mondes, generations, proposeurs, experimentateur, tester_fausses=False):
    k = mondes * generations
    t_pire = 6 * len(proposeurs) + PLANTEES_PIRE + (FAUSSES_ET_COPIES if tester_fausses else 0)
    t_central = 6 + PLANTEES_CENTRAL
    famille = {"opus": "claude", "fable52": "claude", "argon": "argon", "astra": "astra", "kimi": "kimi"}
    lignes = {f: {"central": 0.0, "pire": 0.0} for f in ("claude", "argon", "astra", "kimi")}
    for p in proposeurs:
        lignes[famille[p]]["central"] += CENTRAL_PROPOSEUR[p]
        lignes[famille[p]]["pire"] += PLAFOND_SESSION[p]
    lignes[famille[experimentateur]]["central"] += t_central * 2 * CENTRAL_TOUR[experimentateur]
    lignes[famille[experimentateur]]["pire"] += t_pire * BORNE_TEST[experimentateur]
    lignes["argon"]["central"] += t_central * VERIF_CENTRAL
    lignes["argon"]["pire"] += t_pire * VERIF_PIRE
    out = {f: {"central_usd": round(v["central"] * k, 2), "pire_usd": round(v["pire"] * k, 2)} for f, v in lignes.items()}
    out["total_modeles"] = {"central_usd": round(sum(v["central"] for v in lignes.values()) * k, 2),
                            "pire_usd": round(sum(v["pire"] for v in lignes.values()) * k, 2)}
    out["machine"] = {"central_usd": round(0.15 * k, 2), "plafond_usd": 10.0}
    out["tests_par_generation"] = {"central": t_central, "pire": t_pire}
    return out


def main(argv):
    if len(argv) != 2 or os.path.exists(argv[1]):
        print("usage : devis_multi_generations_v2.py SORTIE.json (neuf)")
        return 2
    quatre = ("opus", "fable52", "argon", "astra")
    res = {"hypotheses": {"prix": PRIX, "plafond_session": PLAFOND_SESSION, "central_proposeur": CENTRAL_PROPOSEUR,
                          "borne_test": BORNE_TEST, "central_tour": {k: round(v, 4) for k, v in CENTRAL_TOUR.items()},
                          "plantees_pire": PLANTEES_PIRE, "plantees_central": PLANTEES_CENTRAL},
           "course": {}}
    for m in (1, 2, 3):
        for e in ("opus", "kimi", "argon"):
            for props, nom in ((quatre, "4"), (quatre + ("kimi",), "5-avec-kimi")):
                for tf in (False, True):
                    res["course"][f"{m}x3|exp={e}|proposeurs={nom}|fausses_testees={tf}"] = course(m, 3, props, e, tf)
    with open(argv[1], "x", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1, sort_keys=True)
    for c in ("1x3|exp=opus|proposeurs=4|fausses_testees=False", "2x3|exp=opus|proposeurs=4|fausses_testees=False",
              "3x3|exp=opus|proposeurs=4|fausses_testees=False", "2x3|exp=opus|proposeurs=5-avec-kimi|fausses_testees=False",
              "2x3|exp=opus|proposeurs=4|fausses_testees=True", "2x3|exp=kimi|proposeurs=5-avec-kimi|fausses_testees=False"):
        print(c, json.dumps(res["course"][c], ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
