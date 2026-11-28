"""Comparaison des sorties de l'extracteur avec mes recalculs — v1.
Écrit APRÈS verif_appariement_v3 et diagnostic_posthoc_v1. Lecture seule.
Usage : python3 -I comparer_extracteur_v1.py DOSSIER_SORTIE
"""
import hashlib
import json
import sys
from pathlib import Path

import numpy as np

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import verif_appariement_v3 as V  # noqa: E402

EXT = Path("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p1-items/extraction")
EMP_EXT = {
    "items-textes-p1-v1.json": "4cb5fe98a4712da0da31c7806449c13310c0c9fb12bf7ae8801015c5ceb43698",
    "prompts-p1-v1.json": "ab4b12a8b997d2bb514f0f4a6151753e5cb5b25c34328813ba555a25d49573ca",
    "gabarit-p1-v1.py": "e666e5de0b516ca66872a4b954af3b61ef0654a2240ea1d3f3bb28eb226eecb4",
    "extraire_items_gabarit_p1_v1.py": "331c73e67a0dc9d27611a3badfe10f52a21589a1f1542941a2ef687d379cb2f0",
    "journal-extraction-p1-v1.txt": "3d3e35e74500133a81b385c430e48610eaff3451cc7845fcf16dfcd6d74f91bf",
}


def h(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def main(sortie):
    res = {"version": "comparer-extracteur-v1"}
    res["empreintes_extracteur"] = {f: V.sha256(EXT / f) == e for f, e in EMP_EXT.items()}
    if not all(res["empreintes_extracteur"].values()):
        raise V.ArretNomme(f"ARRET NOMME empreintes extracteur {res['empreintes_extracteur']}")
    for p, att in V.EMPREINTES.items():
        if V.sha256(p) != att:
            raise V.ArretNomme(f"ARRET NOMME empreinte {p}")

    n200 = json.loads(V.N200.read_text())["texts"]
    c2a = json.loads((V.DONNEES / "c2a_generations.json").read_text())
    c2b = json.loads((V.DONNEES / "c2b_generations.json").read_text())
    press, praise = c2a["meta"]["press"], c2b["meta"]["praise"]
    I = json.loads((EXT / "items-textes-p1-v1.json").read_text())
    P = json.loads((EXT / "prompts-p1-v1.json").read_text())["prompts"]

    # Liste de l'extracteur contre n200[:30]
    textes = [x["texte"] for x in I]
    egaux = lambda t: [k for k, u in enumerate(n200) if u == t]  # noqa: E731
    res["liste"] = {
        "n": len(I),
        "champ_item_egal_rang": all(x["item"] == i for i, x in enumerate(I)),
        "texte_egal_n200_meme_rang": sum(t == n200[i] for i, t in enumerate(textes)),
        "indice_n200_egal_rang": all(x["indice_n200"] == i for i, x in enumerate(I)),
        "indices_egaux_recalcules_conformes": all(x["indices_n200_egaux"] == egaux(x["texte"]) for x in I),
        "indices_egaux_non_triviaux": {x["item"]: x["indices_n200_egaux"] for x in I if len(x["indices_n200_egaux"]) > 1},
        "sha256_texte_conformes": all(x["sha256_texte_utf8"] == h(x["texte"]) for x in I),
        "distincts": len(set(textes)) == len(textes),
        "egal_ma_liste_L": textes == n200[:30],
        "sha256_json_liste_egal_mien": h(json.dumps(textes, ensure_ascii=False)) == h(json.dumps(n200[:30], ensure_ascii=False)),
    }

    # Prompts : texte i dans le prompt i, gabarit uniforme autour du texte
    pr = {"n": len(P), "rang_item_conformes": all(p["item"] == i and p["indice_n200"] == i for i, p in enumerate(P))}
    for champ, phrase, absente in (("neutre", None, "By the way"), ("critique_c2a", press, praise), ("eloge_c2b", praise, press)):
        avant, apres, sha_ok, une_fois, autres_textes = set(), set(), True, True, []
        for i, p in enumerate(P):
            s = p[champ]
            sha_ok &= p["sha256_" + champ] == h(s)
            parts = s.split(textes[i])
            une_fois &= len(parts) == 2
            if len(parts) == 2:
                avant.add(parts[0]); apres.add(parts[1])
            for k, t in enumerate(textes):
                if k != i and t in s and t not in textes[i]:
                    autres_textes.append((i, k))
        a = next(iter(apres)) if len(apres) == 1 else None
        pr[champ] = {
            "sha256_conformes": sha_ok, "texte_i_une_seule_fois": une_fois,
            "prefixe_unique": len(avant) == 1, "suffixe_unique": len(apres) == 1,
            "autre_texte_present": autres_textes,
            "phrase_de_pression_dans_suffixe": (phrase in a) if (a and phrase) else None,
            "phrase_absente_ok": (absente not in a) if a else None,
            "prefixe_sha256": h(next(iter(avant))) if len(avant) == 1 else None,
            "suffixe_sha256": h(a) if a else None,
        }
    res["prompts"] = pr

    # Matrice sur la liste de l'extracteur (doit reproduire mes résultats sur L)
    ML = [V.mots_pleins(t) for t in textes]
    m = {}
    for nom, d in (("c2a", c2a), ("c2b", c2b)):
        reps = [[V.mots_pleins(r["resp"]) for r in sorted((r for r in d["rows"] if r["item"] == j and r["cond"] == "neutral"), key=lambda r: r["k"])] for j in range(30)]
        R = V.matrice(ML, reps)
        lig, col = V.marges(R)
        m[nom] = {"marge_min": round(min(min(lig), min(col)), 4),
                  "colonnes_toutes_dominantes": min(col) > 0, "marge_min_colonnes": round(min(col), 4),
                  "lignes_en_defaut": [i for i, x in enumerate(lig) if x <= 0],
                  "moyenne_diag": round(float(np.diag(R).mean()), 4),
                  "moyenne_hors": round(float(R[~np.eye(30, dtype=bool)].mean()), 4)}
    res["matrice_liste_extracteur"] = m

    out = Path(sortie) / "comparaison-extracteur-v1.json"
    out.write_text(json.dumps(res, ensure_ascii=False, indent=1))
    return res


if __name__ == "__main__":
    print(json.dumps(main(sys.argv[1]), ensure_ascii=False, indent=1))
