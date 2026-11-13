"""Devis v4 de la course à plusieurs générations sur la famille v4 (mots de Lazar R-2492 : Q-1 (b) 2 × 3, Q-12 (i) (a)).
Formule du devis v2 (`../outils-v2/devis_multi_generations_v2.py`, `710954c7…`, importée, inchangée) ; la famille v4 garde au
plus 10 composantes, donc au plus 9 « K1 + un effet » et T_pire = 37 à quatre proposeurs : le pire ne bouge pas. Le central est
refait avec le nombre de représentants promus par génération de la simulation v4 (au lieu de 6). Comparé aux plafonds inscrits
GO-2026-11-13-01 (365 USD sur crédits) et GO-2026-11-13-02 (57 USD hors crédits, machine comprise).
Usage : `python3 -I -B devis_multi_generations_v4.py DOSSIER_SORTIES_V4 SORTIE.json` (lit les parties `partie-v4-monde-*.json`). Bibliothèque standard ; aucun appel."""
import glob
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(ICI), "outils-v2"))
import devis_multi_generations_v2 as D2  # noqa: E402

PLAFOND_CREDITS, PLAFOND_HORS_CREDITS, MACHINE = 365.0, 57.0, 10.0


def main(argv):
    if len(argv) != 3 or os.path.exists(argv[2]):
        print("usage : devis_multi_generations_v4.py DOSSIER_SORTIES_V4 SORTIE.json (neuve)")
        return 2
    parts = [json.load(open(p, encoding="utf-8"))["resultat"] for p in sorted(glob.glob(os.path.join(argv[1], "partie-v4-monde-*.json")))]
    ok = [p for p in parts if p["conforme"]]
    quatre = ("opus", "fable52", "argon", "astra")
    base = D2.course(2, 3, quatre, "opus", False)
    # moyenne des représentants promus, générations 1 à 3 (simulation v4, avec masquage)
    reps = [round(sum(p["masquage"]["generations"][g]["promues"] for p in ok) / len(ok), 2) for g in range(3)]
    t_central = [r + D2.PLANTEES_CENTRAL for r in reps]
    # central : on remplace T_central = 16 par génération par la valeur simulée de chaque génération (2 mondes)
    tour = D2.CENTRAL_TOUR["opus"] * 2
    claude_central = 2 * sum(D2.CENTRAL_PROPOSEUR["opus"] + D2.CENTRAL_PROPOSEUR["fable52"] + t * tour for t in t_central)
    argon_central = 2 * sum(D2.CENTRAL_PROPOSEUR["argon"] + t * D2.VERIF_CENTRAL for t in t_central)
    astra_central = 2 * 3 * D2.CENTRAL_PROPOSEUR["astra"]
    pire_credits = base["claude"]["pire_usd"]
    pire_hors = base["argon"]["pire_usd"] + base["astra"]["pire_usd"] + MACHINE
    out = {"formule": "devis v2 importé, T_pire = %d" % base["tests_par_generation"]["pire"],
           "pire": {"claude_credits": pire_credits, "argon": base["argon"]["pire_usd"], "astra": base["astra"]["pire_usd"],
                    "machine_plafond": MACHINE, "hors_credits_avec_machine": round(pire_hors, 2),
                    "modeles": base["total_modeles"]["pire_usd"]},
           "central_v2_pour_memoire": base["total_modeles"]["central_usd"],
           "central_v4": {"representants_promus_simules": reps, "tests_centraux_par_generation": t_central,
                          "claude": round(claude_central, 2), "argon": round(argon_central, 2), "astra": round(astra_central, 2),
                          "modeles": round(claude_central + argon_central + astra_central, 2),
                          "machine": base["machine"]["central_usd"]},
           "plafonds_inscrits": {"GO-2026-11-13-01": PLAFOND_CREDITS, "GO-2026-11-13-02": PLAFOND_HORS_CREDITS},
           "tient_sous_les_plafonds": {"GO-2026-11-13-01": pire_credits <= PLAFOND_CREDITS,
                                       "GO-2026-11-13-02": pire_hors <= PLAFOND_HORS_CREDITS},
           "marges": {"GO-2026-11-13-01": round(PLAFOND_CREDITS - pire_credits, 2),
                      "GO-2026-11-13-02": round(PLAFOND_HORS_CREDITS - pire_hors, 2)}}
    with open(argv[2], "x", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, sort_keys=True)
    print(json.dumps(out, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
