"""Calibrage du vocabulaire de domaine (v1), avant toute méthode : cherche des paramètres où le vecteur de
domaine code la proximité (cible : même domaine 0,5-0,6 ; proches 0,25-0,35 ; éloignés <= 0,05), pour que les
mondes ordinaires satisfassent l'hypothèse de la forme corrigée. Ne mesure que des cosinus.
Usage : python3 -I -B calibrer_vocabulaire_v1.py
"""
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))
import conditions_v1 as cd
import monde_v1 as mo

GRILLE = [  # premier passage en TF-IDF (proches 0,10-0,16 : rejeté) ; second passage en fréquences brutes
    {"ponderation_domaine": "tfidf", "vocab_champ": 10, "vocab_propre": 6, "mots_domaine": 18, "p_mot_champ": 0.6},
    {"ponderation_domaine": "tf", "vocab_champ": 6, "vocab_propre": 6, "mots_domaine": 14, "p_mot_champ": 0.45},
    {"ponderation_domaine": "tf", "vocab_champ": 8, "vocab_propre": 6, "mots_domaine": 16, "p_mot_champ": 0.5},
    {"ponderation_domaine": "tf", "vocab_champ": 8, "vocab_propre": 8, "mots_domaine": 20, "p_mot_champ": 0.5},
    {"ponderation_domaine": "tf", "vocab_champ": 10, "vocab_propre": 8, "mots_domaine": 20, "p_mot_champ": 0.5},
    {"ponderation_domaine": "tf", "vocab_champ": 8, "vocab_propre": 8, "mots_domaine": 20, "p_mot_champ": 0.45},
]

for reglage in GRILLE:
    sommes = {"meme": [0.0, 0], "proches": [0.0, 0], "eloignes": [0.0, 0]}
    par_f = {}
    for i in range(40):
        w = mo.generer({"niveau": "bien", **reglage}, cd.graine_monde(cd.GRAINE_BASE_VALIDATION, "M_bien", 5000 + i))
        loc = {"meme": [0.0, 0], "proches": [0.0, 0], "eloignes": [0.0, 0]}
        for p in w["paires"]:
            a, b = w["arts"][p["i"]], w["arts"][p["j"]]
            cle = "meme" if a["dom"] == b["dom"] else ("proches" if p["proche"] else "eloignes")
            for s in (sommes[cle], loc[cle]):
                s[0] += w["cos"][p["i"]][p["j"]]
                s[1] += 1
        par_f.setdefault(w["n_champs"], []).append(loc["proches"][0] / max(1, loc["proches"][1]))
    print(reglage, {k: round(v[0] / max(1, v[1]), 3) for k, v in sommes.items()},
          "proches par nombre de champs :", {f: round(sum(v) / len(v), 3) for f, v in sorted(par_f.items())})
