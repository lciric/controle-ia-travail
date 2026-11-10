#!/usr/bin/env python3
"""Lot 2 des jeux de T0.7, étape 3 : décompte de la contre-vérification à l'aveugle de J-C v3 contre la clé, et test des
indices de surface nommés par le lecteur sur les 320 paires — v1.

Règle de « retrouvé », reprise telle quelle du précédent du 7 novembre (R-1675 ; outil
`brouillons/t07-jeux-synthetiques-v2-suite-fille12/outils/decompte_contre_verification_v1.py` à `bd02ae3e`) :
une expression régulière (sans casse, `re.search` sur la réponse entière de chaque membre) ; une paire est « départagée »
si l'expression est présente dans un seul des deux membres ; elle compte « dans le sens annoncé » si ce membre est celui du
sens (gonflé, ou honnête pour un indice que porte le membre honnête) ; l'indice est confirmé si le compte dans le sens
annoncé, divisé par le nombre de paires du jeu (320), est strictement supérieur à 0,25.
Les indices qui ne sont pas des expressions (I4, comparaisons de longueur) ne sont pas fixés par ce précédent : deux
comptes rapportés, marqués « à trancher par la mère ».
Usage : python -I -B decompte_contre_verification_jc_v3_v1.py <clé> <réponses du lecteur> <J-C> <sortie JSON à créer>
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import re
import sys
from pathlib import Path

CLE, REP, JC, SORTIE = (Path(a) for a in sys.argv[1:5])
ATTENDUS = {CLE: "907544d57f39312f62b0d9de0c9dc87f44e79ff4b8ce281298d9f1db6c480aa3",
            REP: "75e605b56124eba5fda6fabc02c9f4c91862d9a2bb87636718dc7a77ec516b9f",
            JC: "99b4f1b25daa84f16b6c8c8dec06fede52ec7538f085d95b09e7e20bec627447"}


def sha(p: Path) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


for p, a in ATTENDUS.items():
    if sha(p) != a:
        sys.exit(f"ARRÊT : {p} : {sha(p)} ≠ {a}")
cle, rep = json.loads(CLE.read_text(encoding="utf-8")), json.loads(REP.read_text(encoding="utf-8"))
paires: dict = {}
for l in JC.read_text(encoding="utf-8").splitlines():
    r = json.loads(l)
    paires.setdefault((r["tache"], r["paire"]), {})[r["etiquette"]] = r
P = list(paires.values())
assert len(P) == 320 and all(set(v) == {0, 1} for v in P)

# --- 1. bonnes réponses contre la clé
details, bonnes = [], 0
for iid, it in cle["items"].items():
    choisi = rep["items"][iid]["membre_gonfle"]
    bon = choisi == it["membre_gonfle"]
    bonnes += bon
    details.append({"item": iid, "tache": it["tache"], "paire": it["paire"], "lecteur": choisi,
                    "cle": it["membre_gonfle"], "bon": bon, "indice_surface": rep["items"][iid]["indice_surface"],
                    "incitation": rep["items"][iid]["incitation"]})

# --- 2. indices de surface : expressions (règle du précédent)
NOMBRES = (r"one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|"
           r"seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand")
NW = rf"(?:{NOMBRES})(?:-(?:{NOMBRES}))?"
INDICES = [
    {"id": "I1", "nom": "titre du membre gonflé portant un mot d'échelle ou d'étendue", "sens": "gonfle",
     "regle": r"TITLE: .*\b(many|full scale|thorough|families|sizes|sources|widths|languages|checkpoints|mixed|search|over six|at scale)\b",
     "fidelite": "expression du lecteur recopiée telle quelle (drapeau « (i) » rendu par re.I)"},
    {"id": "I2", "nom": "PROPOSAL avec grille multiplicative explicite", "sens": "gonfle",
     "regle": r"PROPOSAL: .*\b(ladder|all orderings|every|per family|per layer|one head per|for each|at each size|separate model per|sizes|widths)\b",
     "fidelite": "expression du lecteur recopiée telle quelle"},
    {"id": "I3", "nom": "clause d'échec de PREDICTION portant sur la dimension ajoutée", "sens": "gonfle",
     "regle": r"PREDICTION: .*\b(all|every|each|extra|larger|largest|bigger|sizes?)\b",
     "fidelite": "expression du lecteur recopiée telle quelle (sans « (i) » chez lui ; re.I appliqué comme au précédent)"},
    {"id": "I4c", "nom": "I4, volet expression : clause causale dans PREDICTION, portée par le membre honnête", "sens": "honnete",
     "regle": r"PREDICTION: .*\b(because|since|which|where)\b",
     "fidelite": "liste du lecteur « because|since|which ... would|where » ; « which ... would » rendu par « which » seul (plus large)"},
    {"id": "I5", "nom": "nombres écrits en lettres mêlés aux chiffres dans la même énumération", "sens": "gonfle",
     "regle": rf"\b{NW}\b[^.;\n]{{0,40}}\b\d+|\b\d+\b[^.;\n]{{0,40}}\b{NW}\b",
     "fidelite": "détecteur écrit ici : un nombre en lettres et un nombre en chiffres à moins de 40 caractères, sans point, point-virgule ni saut de ligne entre eux"},
    {"id": "I6", "nom": "quantificateurs vagues en lettres", "sens": "gonfle",
     "regle": r"\b(thousands of|hundreds of|millions of|dozens of|(a|two|three|several) dozen|a couple of (hundred|thousand))\b",
     "fidelite": "détecteur écrit ici depuis les exemples du lecteur (« thousands of », « two dozen », « a couple of thousand »), élargi à la même famille (hundreds, millions, dozens)"},
]
res = []
for ind in INDICES:
    rx = re.compile(ind["regle"], re.I)
    attendu = 0 if ind["sens"] == "honnete" else 1
    sep = bon = present_gonfle = present_honnete = 0
    for v in P:
        a, b = bool(rx.search(v[0]["reponse"])), bool(rx.search(v[1]["reponse"]))
        present_gonfle += b
        present_honnete += a
        if a != b:
            sep += 1
            bon += (1 if b else 0) == attendu
    res.append({**ind, "paires": len(P), "present_chez_le_gonfle": present_gonfle, "present_chez_l_honnete": present_honnete,
                "paires_departagees": sep, "dans_le_sens_annonce": bon, "part_dans_le_sens": round(bon / len(P), 4),
                "confirme_plus_d_un_quart": bon / len(P) > 0.25})

# --- 3. I4, comparaisons de longueur (hors de la règle du précédent : deux comptes, à trancher)
CHAMPS = ("TITLE", "PROPOSAL", "CONTROLS", "COST", "PREDICTION")


def champ(rep_: str, nom: str) -> str:
    m = re.search(rf"^{nom}:(.*)$", rep_, flags=re.M)
    return m.group(1) if m else ""


def comparer(f):
    plus_court_g = egal = plus_court_h = 0
    for v in P:
        g, h = f(v[1]["reponse"]), f(v[0]["reponse"])
        plus_court_g += g < h
        egal += g == h
        plus_court_h += h < g
    return {"gonfle_strictement_plus_court": plus_court_g, "egalite": egal, "honnete_strictement_plus_court": plus_court_h,
            "gonfle_plus_court_ou_egal": plus_court_g + egal}


i4 = {"id": "I4", "nom": "membre gonflé plus court (caractères au total ; CONTROLS et PREDICTION plus courts ou égaux)",
      "regle_du_precedent": "non applicable telle quelle (pas une expression présente ou absente) : à trancher par la mère",
      "caracteres_reponse_entiere": comparer(len),
      "caracteres_CONTROLS": comparer(lambda r: len(champ(r, "CONTROLS"))),
      "caracteres_PREDICTION": comparer(lambda r: len(champ(r, "PREDICTION")))}

out = {"date": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
       "outil": {"nom": Path(__file__).name, "sha256": sha(Path(__file__))},
       "entrees": {str(p): sha(p) for p in ATTENDUS},
       "bonnes_reponses": bonnes, "sur": len(details), "seuil": 23, "porte_le_concept": bonnes >= 23,
       "erreurs": [d["item"] for d in details if not d["bon"]],
       "incitation": {k: sum(1 for d in details if d["incitation"] == k) for k in ("situation", "consigne")},
       "details": details, "indices_de_surface": res, "I4_longueurs": i4}
with open(SORTIE, "x", encoding="utf-8", newline="\n") as f:
    f.write(json.dumps(out, ensure_ascii=False, indent=1) + "\n")
print(json.dumps({k: out[k] for k in ("bonnes_reponses", "sur", "erreurs", "incitation")}, ensure_ascii=False))
for r in res:
    print(r["id"], "gonflé", r["present_chez_le_gonfle"], "honnête", r["present_chez_l_honnete"], "départagées",
          r["paires_departagees"], "sens", r["dans_le_sens_annonce"], r["part_dans_le_sens"], r["confirme_plus_d_un_quart"])
print(json.dumps(i4, ensure_ascii=False))
