"""Vérification des corrections de la batterie (v3) — la règle de trois instances au hasard, recalculée — v1.

Écrit par le vérificateur des corrections (Opus 5.5, session neuve), sans importer le code du concepteur
(`sondes_batterie_v2.py`, `calcul_5_version_6_v2.py`) : la probabilité exacte, le tirage de contrôle et la borne
haute sont recodés ici d'après la lettre du § 1, C4, et du § 0 de `batterie-fuite-banque-revisee-v3.md`.
Le paquet de la version 6 sert seulement à engendrer les banques des 41 racines d'essai déjà exposées (0 à 39 et
20261122 ; aucune autre racine du générateur) et à énumérer les instances par sa vérification exacte (`parcourir`).
Processeur seul ; aucun appel de modèle ; aucun fichier de clé lu (la clé de sous-banque reste en mémoire).

Partie A : cas simples (formule fermée, produit des tirages sans remise, énumération de tous les triplets).
Partie B : la table de la sortie du calcul 5 (N = 4, 10, 15 ; une variable naturelle).
Partie C : la version 6 sur ses 41 racines d'essai ; comparaison racine par racine à `sortie-calcul-5-v2.json`.

Emploi : OMP_NUM_THREADS=1 PYTHONPATH=<dépôt>/src python3 verif_regle_du_hasard_v1.py SORTIE.json > SORTIE.txt
"""
import itertools, json, math, sys
from fractions import Fraction
from pathlib import Path

import numpy as np

ICI = Path(__file__).resolve().parent
SORTIE_5 = ICI.parent / "calculs-d-appui" / "sortie-calcul-5-v2.json"
RACINES_V6 = list(range(40)) + [20261122]


# ------------------------------------------------------------------ trois façons de calculer la même probabilité
def p_formule(M, m):
    """Lettre du § 1, C4 : 1 − C(M − m, 3)/C(M, 3) ; 1 si M ≤ 3 et m ≥ 1 ; 0 si m = 0."""
    if m == 0:
        return Fraction(0)
    if M <= 3:
        return Fraction(1)
    return 1 - Fraction(math.comb(M - m, 3), math.comb(M, 3))


def p_produit(M, m):
    """Trois tirages successifs sans remise : probabilité qu'aucun ne soit un contre-exemple, par produit."""
    k = min(3, M)
    q = Fraction(1)
    for i in range(k):
        q *= Fraction(M - m - i, M - i) if M - m - i > 0 else 0
    return 1 - q


def p_enumeration(M, m):
    """Tous les sous-ensembles de min(3, M) instances parmi M ; contre-exemples aux rangs 0..m−1."""
    k = min(3, M)
    tous = list(itertools.combinations(range(M), k))
    return Fraction(sum(1 for t in tous if min(t) < m), len(tous))


def borne_haute(valeurs, j):
    """§ 0 : 95e centile de 2 000 moyennes rééchantillonnées avec remise ; graine SeedSequence(20261122, (2000 + j,))."""
    v = np.asarray(valeurs, float)
    g = np.random.default_rng(np.random.SeedSequence(20261122, spawn_key=(2000 + j,)))
    return float(np.quantile(v[g.integers(0, len(v), size=(2000, len(v)))].mean(axis=1), 0.95))


def partie_A():
    out = {"cas": {}}
    cas = {"un contre-exemple parmi 13": (13, 1), "M = 3, m = 1": (3, 1), "M = 2, m = 1": (2, 1),
           "faux sans variable (M = 1, m = 1)": (1, 1), "aucun contre-exemple (13, 0)": (13, 0),
           "M = 4, m = 1": (4, 1), "M = 31, m = 6": (31, 6), "M = 46, m = 9": (46, 9)}
    for nom, (M, m) in cas.items():
        a, b, c = p_formule(M, m), p_produit(M, m), p_enumeration(M, m)
        out["cas"][nom] = {"M": M, "m": m, "formule": str(a), "valeur": round(float(a), 6),
                           "produit_egal": a == b, "enumeration_egale": a == c}
    ecarts = 0
    for M in range(1, 41):
        for m in range(0, M + 1):
            if not (p_formule(M, m) == p_produit(M, m) == p_enumeration(M, m)):
                ecarts += 1
    out["balayage_M_1_a_40_tous_m"] = {"ecarts": ecarts}
    # repère « la part passe la moitié quand une instance sur cinq environ est un contre-exemple »
    out["plus_petit_m_au_dessus_de_la_moitie"] = {M: next(m for m in range(M + 1) if p_formule(M, m) > Fraction(1, 2))
                                                  for M in (13, 31, 46)}
    return out


def partie_B(s5):
    out = {}
    for N in (4, 10, 15):
        M = 3 * N + 1
        cle = f"N={N}, M={M}"
        mien = {f"m={m}": round(float(p_formule(M, m)), 3) for m in (1, 2, 3, 4, 6, 8, 12, 16, 24) if m <= M}
        queue = [p_formule(M, 3 * N - n0 + 1) for n0 in range(N + 1, 3 * N + 1)]
        mien["piege_en_queue_moyenne"] = round(float(sum(queue) / len(queue)), 3)
        out[cle] = {"mien": mien, "calcul_5": s5["table_du_hasard"][cle], "identique": mien == s5["table_du_hasard"][cle]}
    return out


def partie_C(s5):
    from controle_ia.oracles_plantes_v6 import banque as pk_banque
    from controle_ia.oracles_plantes_v6 import parametres as pk_parametres
    from controle_ia.oracles_plantes_v6.evaluation import parcourir, prefixe
    from controle_ia.oracles_plantes_v6.graines import generateur
    from controle_ia.oracles_plantes_v6.sous_banque import identifiants_opaques, tirer_sous_banque

    params, sha = pk_parametres.charger()
    lignes_5 = {l["racine"]: l for l in s5["lignes"]}
    res, stat = [], {"instances_H_completes": 0, "affectations_partielles": 0, "faux": 0, "M_max": 0,
                     "faux_sans_variable": 0, "faux_M_le_3": 0}
    for rang, r in enumerate(RACINES_V6):
        B = pk_banque.construire_banque(r, params)
        ids = identifiants_opaques(generateur(r, 3, 0), len(B), "monde-")
        _servie, cle_sb = tirer_sous_banque(B, ids, r, params["sous_banque"])
        index = {}
        for w, (m, plantes) in enumerate(B):
            for p in plantes:
                index[(ids[w], p.etiquette, p.gabarit)] = (m, p)
        faux = []
        for c in cle_sb["items"]:
            if c["role"] != "analyse":
                continue
            m, p = index[(c["identifiant_monde"], c["etiquette"], c["gabarit"])]
            if p.etiquette in ("FAUX_TOT", "PIEGE"):  # étiquettes de faux du paquet de la version 6
                faux.append((m, p))
        etiquettes = sorted({p.etiquette for _, p in faux})
        exact, tirage, par_et = [], [], {}
        for k, (m, p) in enumerate(faux):
            arbre = m.analyser(p.texte)
            pre, _ = prefixe(arbre)
            statuts = []
            for inst, st in parcourir(m.ev, arbre, m.borne_verification()):
                if len(inst) == len(pre):
                    statuts.append(st)
                    stat["instances_H_completes"] += (st == "H")
                else:
                    stat["affectations_partielles"] += 1
            M = len(statuts)
            mm = sum(1 for st in statuts if st in ("F", "I"))
            stat["faux"] += 1
            stat["M_max"] = max(stat["M_max"], M)
            stat["faux_sans_variable"] += (len(pre) == 0)
            stat["faux_M_le_3"] += (M <= 3)
            pr = p_formule(M, mm)
            assert pr == p_produit(M, mm)
            exact.append(pr)
            par_et.setdefault(p.etiquette, []).append(pr)
            # tirage de contrôle, lettre du § 1, C4 : i = rang de la racine, k = rang du faux dans la sous-banque
            g = np.random.default_rng(np.random.SeedSequence(20261122, spawn_key=(3000, rang, k)))
            tirage.append(any(statuts[int(i)] in ("F", "I") for i in g.choice(M, size=min(3, M), replace=False)) if M else False)
        l5 = lignes_5[r]
        ligne = {"racine": r, "nombre_de_faux": len(faux), "etiquettes": etiquettes,
                 "v_hasard": float(sum(exact) / len(exact)), "v_hasard_tirage": float(np.mean(tirage)),
                 "par_etiquette": {e: float(sum(v) / len(v)) for e, v in par_et.items()}}
        ligne["ecart_v_hasard_au_calcul_5"] = abs(ligne["v_hasard"] - l5["v_hasard"])
        ligne["ecart_tirage_au_calcul_5"] = abs(ligne["v_hasard_tirage"] - l5["v_hasard_tirage"])
        res.append(ligne)
        print(f"  racine {r}: {len(faux)} faux, hasard exact {ligne['v_hasard']:.4f} "
              f"(calcul 5 : {l5['v_hasard']:.4f}), tirage {ligne['v_hasard_tirage']:.4f} (calcul 5 : {l5['v_hasard_tirage']:.4f})",
              file=sys.stderr, flush=True)
    v = [l["v_hasard"] for l in res]
    out = {"parametres_sha256": sha, "racines": RACINES_V6, "statistiques": stat,
           "moyenne": round(float(np.mean(v)), 4), "min": round(min(v), 4), "max": round(max(v), 4),
           "borne_haute_j11": round(borne_haute(v, 11), 4),
           "calcul_5_C4_regle_du_hasard": s5["C4"]["regle_du_hasard_exacte"],
           "plus_grand_ecart_par_racine_exact": max(l["ecart_v_hasard_au_calcul_5"] for l in res),
           "plus_grand_ecart_par_racine_tirage": max(l["ecart_tirage_au_calcul_5"] for l in res),
           "moyenne_tirage": round(float(np.mean([l["v_hasard_tirage"] for l in res])), 4),
           "ecart_tirage_exact": round(abs(float(np.mean([l["v_hasard_tirage"] for l in res])) - float(np.mean(v))), 4),
           "lignes": res}
    for e in sorted({e for l in res for e in l["par_etiquette"]}):
        ve = [l["par_etiquette"][e] for l in res if e in l["par_etiquette"]]
        out[f"moyenne_{e}"] = round(float(np.mean(ve)), 4)
    return out


def main(chemin):
    s5 = json.loads(SORTIE_5.read_text(encoding="utf-8"))
    out = {"numpy": np.__version__, "A": partie_A(), "B": partie_B(s5)}
    print("Vérification de la règle de trois instances au hasard (batterie v3) — v1")
    print(f"numpy {np.__version__}")
    print("A. cas simples")
    for k, v in out["A"]["cas"].items():
        print(f"  {k:36s} : {v}")
    print(f"  balayage M = 1 à 40, tous m : {out['A']['balayage_M_1_a_40_tous_m']}")
    print(f"  plus petit m au-dessus de la moitié : {out['A']['plus_petit_m_au_dessus_de_la_moitie']}")
    print("B. table du calcul 5")
    for k, v in out["B"].items():
        print(f"  {k} : identique {v['identique']} ; mien {v['mien']}")
    out["C"] = partie_C(s5)
    c = out["C"]
    print("C. version 6, 41 racines d'essai")
    for k in sorted(c):
        if k != "lignes":
            print(f"  {k} : {c[k]}")
    with open(chemin, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1, sort_keys=True, default=str)
        fh.write("\n")


if __name__ == "__main__":
    main(sys.argv[1])
