"""Accords entre modèles et indépendance effective, par paires d'espèces, sur les dossiers communs.

Trois mesures, chacune avec un test par permutation des étiquettes d'espèce à l'intérieur de chaque
course (graines par numpy.random.SeedSequence) :
 (a) proximité des conceptions indépendantes du tour 1 (similarité de mots, formules et balises retirées) ;
 (b) proximité des « expériences à faire en premier » du dernier tour ;
 (c) co-soutien des propositions retenues (lettres porteuses déclarées par la note de sortie).
Statistique d'indépendance : écart moyen « même fournisseur » moins « fournisseurs différents ».
Sortie : sorties/accords-v1.json.
"""
import itertools
import json
import re
import sys
from collections import defaultdict

import numpy as np

from audit_commun_v2 import SORTIES, ESPECE_FOURNISSEUR, Tfidf, cos, graine, inventaire
from cellules_v1 import charger

N_PERM = 10000


def nettoyer(t):
    t = re.sub(r"\$[^$]*\$", " ", t)              # formules en ligne
    t = re.sub(r"\\[a-zA-Z]+", " ", t)            # commandes de composition
    t = re.sub(r"`[^`]*`", " ", t)                # balises et chemins entre accents graves
    t = re.sub(r"\b(V[ÉE]RIFI[ÉE]|RAPPORT[ÉE]|HYPOTH[ÈE]SE|illustratif|OBSERV[ÉE]-NON-AUDIT[ÉE])\b", " ", t, flags=re.I)
    return t


def paires_par_course(textes_par_course):
    """textes_par_course : {racine: {espece: texte}} -> [(racine, e1, e2, sim)]"""
    tous = [t for d in textes_par_course.values() for t in d.values()]
    tf = Tfidf(tous)
    out = []
    for r, d in textes_par_course.items():
        vec = {e: tf.vec(t) for e, t in d.items()}
        for e1, e2 in itertools.combinations(sorted(vec), 2):
            out.append((r, e1, e2, cos(vec[e1], vec[e2])))
    return out


def meme(e1, e2):
    f1, f2 = ESPECE_FOURNISSEUR.get(e1, e1), ESPECE_FOURNISSEUR.get(e2, e2)
    return f1 == f2


def statistique(lignes):
    """Moyenne sur les courses (qui ont les deux sortes de paires) de (moyenne même − moyenne différent)."""
    parc = defaultdict(lambda: ([], []))
    for r, e1, e2, s in lignes:
        parc[r][0 if meme(e1, e2) else 1].append(s)
    d = [np.mean(a) - np.mean(b) for a, b in parc.values() if a and b]
    return (float(np.mean(d)) if d else None), len(d)


def permutation(lignes, tache):
    rng, meta = graine(tache)
    obs, n = statistique(lignes)
    if obs is None:
        return {"observe": None, "courses": 0, "graine": meta}
    par = defaultdict(list)
    for x in lignes:
        par[x[0]].append(x)
    plus = 0
    for _ in range(N_PERM):
        perm = []
        for r, L in par.items():
            esp = sorted({e for _, a, b, _ in L for e in (a, b)})
            p = dict(zip(esp, rng.permutation(esp)))
            perm += [(r, p[a], p[b], s) for _, a, b, s in L]
        v, _ = statistique(perm)
        if v is not None and v >= obs:
            plus += 1
    return {"observe": round(obs, 4), "courses": n, "p_unilaterale": round((plus + 1) / (N_PERM + 1), 4),
            "permutations": N_PERM, "graine": meta}


def matrice(lignes):
    m = defaultdict(list)
    for r, e1, e2, s in lignes:
        m[f"{e1}~{e2}"].append(s)
    return {k: {"moyenne": round(float(np.mean(v)), 4), "dossiers_communs": len(v), "meme_fournisseur": meme(*k.split("~"))}
            for k, v in sorted(m.items())}


def main():
    C = [c for c in charger() if not c["rejeu_de"]]
    # (a) tour 1
    t1 = defaultdict(dict)
    for c in C:
        if c["tour"] == 1 and c["role"] == "conception":
            t1[c["racine"]][c["espece"]] = nettoyer(c["texte"])
    la = paires_par_course({r: d for r, d in t1.items() if len(d) >= 3})
    # (b) premiers choix
    U = json.loads((SORTIES / "unites-v1.json").read_text())
    pc = defaultdict(dict)
    for p in U["premiers"]:
        if not p["rejeu_de"]:
            pc[p["racine"]][p["espece"]] = nettoyer(p["texte"])
    lb = paires_par_course({r: d for r, d in pc.items() if len(d) >= 3})
    # (c) co-soutien des retenues
    J = json.loads((SORTIES / "jeu-des-propositions-v1.json").read_text())
    inv = {d["racine"]: d for d in inventaire()}
    co = defaultdict(lambda: defaultdict(lambda: [0, 0, 0, 0]))  # course -> paire -> [les deux, e1 seul, e2 seul, aucun]
    for j in J:
        if j["genre"] != "retenue" or j["attribution"] != "déclarée" or not j["dossier"]:
            continue
        esp = sorted({v.get("espece") for v in inv[j["dossier"]]["lettres"].values() if v.get("espece") not in (None, "inconnu")})
        port = set(j["especes_porteuses"])
        for e1, e2 in itertools.combinations(esp, 2):
            k = (e1 in port) * 2 + (e2 in port)
            co[j["dossier"]][(e1, e2)][{3: 0, 2: 1, 1: 2, 0: 3}[k]] += 1
    lc = []
    for r, d in co.items():
        for (e1, e2), (ab, a, b, n0) in d.items():
            tot = ab + a + b + n0
            if tot >= 3:
                lc.append((r, e1, e2, (ab + n0) / tot))  # accord simple sur « soutient ou non »
    out = {
        "conceptions_tour1": {"matrice": matrice(la), "test": permutation(la, "accords-tour1")},
        "premiers_choix": {"matrice": matrice(lb), "test": permutation(lb, "accords-premiers")},
        "co_soutien_retenues": {"matrice": matrice(lc), "test": permutation(lc, "accords-cosoutien"),
                                "definition": "accord simple sur « porte ou ne porte pas » une retenue, par dossier"},
    }
    (SORTIES / "accords-v1.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
    for k, v in out.items():
        print("==", k, v["test"])
        for p, m in v["matrice"].items():
            if m["dossiers_communs"] >= 3:
                print("  ", p, m)
    return 0


if __name__ == "__main__":
    sys.exit(main())
