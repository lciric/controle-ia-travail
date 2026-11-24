"""Fidélité : rejeux et bras jumeaux.

1. Rejeux d'Argon (cinq courses rejouées sur la v8d) : similarité entre la cellule rejouée et la cellule
   d'origine du même tour, comparée aux similarités entre espèces différentes dans la course d'origine.
2. Bras jumeaux : « question générale » isolée contre son jumeau en abonnement ; boucle organisme-contrôle,
   bras principal contre bras témoin (question posée autrement). Même espèce d'un bras à l'autre, contre
   espèces différentes dans un même bras.
3. Propositions retenues du bras général contre celles du jumeau : appariement par similarité, à relire.
Sortie : sorties/fidelite-v1.json.
"""
import itertools
import json
import sys
from collections import defaultdict

import numpy as np

from audit_commun_v2 import SORTIES, Tfidf, cos
from cellules_v1 import charger
from accords_v1 import nettoyer

PAIRES_BRAS = [
    ("runs/collisionneur-protocole-x-generale-isole-v1-20261122-080928",
     "runs/collisionneur-protocole-x-generale-isole-jumeau-abonnement-v1-20261122-142638", "question générale : isolé contre jumeau"),
    ("docs/notes/collisionneurs-reprise-2026-11-24-v1/boucle-organisme-controle/principal",
     "docs/notes/collisionneurs-reprise-2026-11-24-v1/boucle-organisme-controle/temoin", "boucle organisme-contrôle : principal contre témoin"),
]


def main():
    C = charger()
    tf = Tfidf([nettoyer(c["texte"]) for c in C])
    V = {c["chemin"]: tf.vec(nettoyer(c["texte"])) for c in C}
    idx = defaultdict(dict)
    for c in C:
        idx[c["racine"]][(c["espece"], c["tour"])] = c
    out = {"rejeux": [], "bras": [], "retenues_jumeau": []}
    for r, d in idx.items():
        orig = next((c["rejeu_de"] for c in d.values() if c["rejeu_de"]), None)
        if not orig:
            continue
        for (e, t), c in d.items():
            o = idx.get(orig, {}).get((e, t))
            if not o:
                continue
            autres = [cos(V[o["chemin"]], V[x["chemin"]]) for (e2, t2), x in idx[orig].items() if t2 == t and e2 != e]
            out["rejeux"].append({"course": orig, "espece": e, "tour": t,
                                  "sim_rejeu_origine": round(cos(V[c["chemin"]], V[o["chemin"]]), 4),
                                  "sim_origine_autres_especes_moyenne": round(float(np.mean(autres)), 4) if autres else None,
                                  "sim_origine_autres_especes_max": round(float(np.max(autres)), 4) if autres else None})
    for a, b, nom in PAIRES_BRAS:
        meme, diff = [], []
        for t in (1, 3):
            ea = {e: c for (e, tt), c in idx.get(a, {}).items() if tt == t}
            eb = {e: c for (e, tt), c in idx.get(b, {}).items() if tt == t}
            for e in sorted(set(ea) & set(eb)):
                meme.append((t, e, cos(V[ea[e]["chemin"]], V[eb[e]["chemin"]])))
            for e1, e2 in itertools.combinations(sorted(ea), 2):
                diff.append((t, e1 + "~" + e2, cos(V[ea[e1]["chemin"]], V[ea[e2]["chemin"]])))
        out["bras"].append({"paire": nom, "meme_espece_entre_bras": [(t, e, round(s, 4)) for t, e, s in meme],
                            "especes_differentes_meme_bras": [(t, e, round(s, 4)) for t, e, s in diff],
                            "moyenne_meme": round(float(np.mean([s for *_, s in meme])), 4) if meme else None,
                            "moyenne_diff": round(float(np.mean([s for *_, s in diff])), 4) if diff else None})
    J = json.loads((SORTIES / "jeu-des-propositions-v1.json").read_text())
    ga = [j for j in J if j["genre"] == "retenue" and j["dossier"] == PAIRES_BRAS[0][0]]
    gb = [j for j in J if j["genre"] == "retenue" and j["dossier"] == PAIRES_BRAS[0][1]]
    tf2 = Tfidf([j["texte"] for j in ga + gb])
    for j in gb:
        best = max(((cos(tf2.vec(j["texte"]), tf2.vec(k["texte"])), k) for k in ga), key=lambda x: x[0], default=(0, None))
        out["retenues_jumeau"].append({"jumeau": j["id"], "texte_jumeau": j["texte"][:160],
                                       "meilleur_isole": best[1]["id"] if best[1] else None,
                                       "texte_isole": best[1]["texte"][:160] if best[1] else None, "sim": round(best[0], 4)})
    (SORTIES / "fidelite-v1.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
    for x in out["rejeux"]:
        print(x)
    for x in out["bras"]:
        print(x["paire"], x["moyenne_meme"], x["moyenne_diff"], x["meme_espece_entre_bras"])
    for x in out["retenues_jumeau"]:
        print(x["sim"], "|", x["texte_jumeau"][:90], "||", (x["texte_isole"] or "")[:90])
    return 0


if __name__ == "__main__":
    sys.exit(main())
