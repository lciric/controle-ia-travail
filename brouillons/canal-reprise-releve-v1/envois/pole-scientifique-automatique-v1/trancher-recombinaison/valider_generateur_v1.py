"""Validation du générateur (v1) : propriétés des mondes seulement, aucune méthode n'est lancée.
Graines de validation distinctes des graines principales. Vérifie que les mondes ordinaires satisfont
l'hypothèse de la forme corrigée (domaines bien séparés dans le vecteur de domaine) et décrit la population
des paires valides (ce que toutes les méthodes peuvent tirer).
Usage : python3 -I -B valider_generateur_v1.py --heure "$(date -u +%Y-%m-%dT%H:%M:%SZ)" [--mondes 100]
"""
import argparse
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))
import conditions_v1 as cd
import mesures_v1 as ms
import monde_v1 as mo

SORTIE = Path(__file__).resolve().parent


def stats_monde(w):
    arts, paires, df = w["arts"], w["paires"], ms.frequences_etiquettes(w)
    cos = {"meme_domaine": [], "proches": [], "eloignes": []}
    for p in paires:
        a, b = arts[p["i"]], arts[p["j"]]
        cle = "meme_domaine" if a["dom"] == b["dom"] else ("proches" if p["proche"] else "eloignes")
        cos[cle].append(w["cos"][p["i"]][p["j"]])
    valides = w["valides"]
    classes = Counter(ms.classe_pont(w, x, ms.etiquette_pont(w, x, df)) for x in valides)
    rel = Counter("meme_domaine" if arts[paires[x]["i"]]["dom"] == arts[paires[x]["j"]]["dom"]
                  else ("proches" if paires[x]["proche"] else "eloignes") for x in valides)
    vus = tot = 0
    for a in arts:
        for o in a["ops"]:
            tot += 1
            vus += int(a["etiquettes"].get(o) == "vrai")
    cand = [p for p in paires if arts[p["i"]]["dom_obs"] != arts[p["j"]]["dom_obs"] and p["partage"]]
    incompat = [p for p in cand if not p["compat_vraie"]]
    compat = [p for p in cand if p["compat_vraie"]]
    rejet = lambda p: not p["valide"]
    nv = len(valides)
    return {
        "cos_meme_domaine": sum(cos["meme_domaine"]) / max(1, len(cos["meme_domaine"])),
        "cos_proches": sum(cos["proches"]) / max(1, len(cos["proches"])) if cos["proches"] else None,
        "cos_eloignes": sum(cos["eloignes"]) / max(1, len(cos["eloignes"])),
        "n_champs": w["n_champs"], "n_valides": nv, "n_vrais": len(w["vrais"]),
        "n_vrais_valides": len(w["vrais"] & set(valides)),
        "taux_de_base": len(w["vrais"] & set(valides)) / nv if nv else None,
        "valides_proches": rel["proches"] / nv if nv else None,
        "valides_eloignes": rel["eloignes"] / nv if nv else None,
        "valides_meme_domaine": rel["meme_domaine"] / nv if nv else None,
        **{f"valides_classe_{c}": classes[c] / nv if nv else None
           for c in ("vrai_op", "moyeu", "homonyme", "parasite", "autre", "sans_etiquette")},
        "rappel_etiquettes": vus / tot if tot else None,
        "part_incompatibles_candidates": len(incompat) / len(cand) if cand else None,
        "rappel_filtre": sum(1 for p in incompat if rejet(p)) / len(incompat) if incompat else None,
        "rejets_a_tort": sum(1 for p in compat if rejet(p)) / len(compat) if compat else None,
        "n_plantes": len(w["plantes"]), "n_homonymes": w["n_homonymes"],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--heure", required=True)
    ap.add_argument("--mondes", type=int, default=100)
    args = ap.parse_args()
    resultats = {}
    for nom, params in {**cd.CONDITIONS, **cd.SENSIBILITE}.items():
        lignes = [stats_monde(mo.generer(params, cd.graine_monde(cd.GRAINE_BASE_VALIDATION, nom, i)))
                  for i in range(args.mondes)]
        moy = {}
        for cle in lignes[0]:
            vals = [l[cle] for l in lignes if l[cle] is not None]
            moy[cle] = sum(vals) / len(vals) if vals else None
        resultats[nom] = moy
        print(nom, {k: (round(v, 3) if isinstance(v, float) else v) for k, v in moy.items()})
    sortie = {"objet": "validation du générateur (propriétés des mondes, aucune méthode)",
              "heure_lancement_utc": args.heure, "python": sys.version.split()[0],
              "graines": f"random.Random(GRAINE_BASE_VALIDATION + 100000 x id_condition + i), base {cd.GRAINE_BASE_VALIDATION}",
              "mondes_par_condition": args.mondes, "base": {k: v for k, v in mo.BASE.items()},
              "niveaux": mo.NIVEAUX, "conditions": {**cd.CONDITIONS, **cd.SENSIBILITE}, "resultats": resultats}
    (SORTIE / "validation-generateur-v1.json").write_text(json.dumps(sortie, ensure_ascii=False, indent=1) + "\n",
                                                          encoding="utf-8")


if __name__ == "__main__":
    main()
