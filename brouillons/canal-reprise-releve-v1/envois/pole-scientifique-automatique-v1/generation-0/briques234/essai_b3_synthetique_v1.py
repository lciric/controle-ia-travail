"""Brique 3, essai 4 (corpus synthétiques) : seuil d'entrée du pivot, remèdes, coût du graphe de ligne.

Partie 1 : textes A et C (vocabulaires disjoints), pivot B dans m des n textes (f = m/n de 0,3 à 1),
k mots-outils présents partout ; P(B dans termes_satures) par la copie exacte de la fonction de l'organisme.
Partie 2 : vérité terrain (B à retenir, hub générique H à repousser, mots-outils à ignorer) ; remèdes
(a) liste d'arrêt, (b) exemption des ponts entre groupes contrastés, (b+) idem avec fréquence de fond,
(c) répulsion sur paires co-occurrentes (nœuds du graphe de ligne).
Partie 3 : arêtes du graphe de ligne passant par B en fonction de son degré d_B (comptage explicite).
Usage : python3 -I -B essai_b3_synthetique_v1.py --heure "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
"""
import argparse
import math
import sys
import time
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))
import numpy as np

import commun_v1 as cm
import textes_v1 as tx

GRAINES = 200
TAILLES_N = [5, 10, 20]
K_OUTILS = [0, 3, 6, 12]
PIVOTS = ["magnesium", "calcium"]
HUB = "modele"


def vocab_graine(s: int):
    return tx.pseudo_mots(cm.generateur("b3_seuil", 999, s), 120, {"magnesium", "calcium", HUB})


def partie_seuil(capacite):
    res = []
    vocabs = [vocab_graine(s) for s in range(GRAINES)]
    for n in TAILLES_N:
        for m in range(math.ceil(0.3 * n), n + 1):
            for k in K_OUTILS:
                for pid, pivot in enumerate(PIVOTS):
                    entre = 0
                    for s in range(GRAINES):
                        rng = cm.generateur("b3_seuil", n, m, k, pid, s)
                        textes, _, _ = tx.corpus_ponts(rng, n, m, k, pivot=pivot, vocab=vocabs[s])
                        entre += int(pivot in capacite(textes)["termes_satures"])
                    res.append({"n": n, "m": m, "f": round(m / n, 4), "k_outils": k, "pivot": pivot,
                                "seuil_textes": tx.seuil_saturation(n), "p_pivot_sature": entre / GRAINES})
    return res


def corpus_fond(s: int):
    """Fond : 300 textes de 10 autres domaines ; hub fréquent (0,8), pivot rare (0,01)."""
    rng = cm.generateur("b3_remedes", 777, s)
    vocab = tx.pseudo_mots(rng, 400, {"magnesium", HUB})
    poids = 1.0 / np.arange(1, 41) ** 1.1
    poids /= poids.sum()
    docs = []
    for i in range(300):
        v = vocab[(i % 10) * 40:(i % 10 + 1) * 40]
        mots = list(rng.choice(v, size=60, p=poids))
        if rng.random() < 0.8:
            mots.append(HUB)
        if rng.random() < 0.01:
            mots.append("magnesium")
        docs.append([t for t in tx.jetons(" ".join(mots)) if not tx.est_arret(t)])
    df = tx.frequences_document(docs)
    return {t: c / len(docs) for t, c in df.items()}


def partie_remedes(capacite):
    res = []
    fonds = [corpus_fond(s) for s in range(GRAINES)]
    vocabs = [vocab_graine(s) for s in range(GRAINES)]
    for n in TAILLES_N:
        for f in (0.6, 0.8, 1.0):
            m = max(1, round(f * n))
            for k in (0, 12):
                acc = {}
                for s in range(GRAINES):
                    rng = cm.generateur("b3_remedes", n, m, k, s)
                    textes, _, _ = tx.corpus_ponts(rng, n, m, k, pivot="magnesium", hub=HUB, p_hub=0.9, vocab=vocabs[s])
                    sorties = {"base": capacite(textes)["termes_satures"], "a_arret": tx.remede_a(textes, capacite)}
                    for tau in (0.5, 0.7, 0.9):
                        sorties[f"b_tau_{tau}"] = tx.remede_b(textes, tau=tau)["termes_satures"]
                    sorties["b_plus_tau_0.7"] = tx.remede_b(textes, tau=0.7, fond_df=fonds[s], beta=0.1)["termes_satures"]
                    for arret in (False, True):
                        rc = tx.remede_c(textes, "cooccurrence", arret)
                        sorties[f"c_paires_{'arret' if arret else 'brut'}"] = rc["paires_saturees"]
                        acc.setdefault(f"cout_c_paires_{'arret' if arret else 'brut'}", []).append(rc["paires_comptees"])
                    acc.setdefault("cout_termes", []).append(sum(len(set(tx.jetons(x))) for x in textes))
                    for nom, lst in sorties.items():
                        est_paire = nom.startswith("c_")
                        contient = (lambda w: any(w in p for p in lst)) if est_paire else (lambda w: w in lst)
                        outil = [any(tx.est_arret(w) for w in p) if est_paire else tx.est_arret(p) for p in lst]
                        a = acc.setdefault(nom, {"pivot": 0, "hub": 0, "outils": [], "vide": 0, "pont_bloque": 0})
                        if est_paire:
                            a["pont_bloque"] += int(any("magnesium" in p and not any(tx.est_arret(w) or w == HUB for w in p if w != "magnesium")
                                                        for p in lst))
                        else:
                            a["pont_bloque"] += int("magnesium" in lst)
                        a["pivot"] += int(contient("magnesium"))
                        a["hub"] += int(contient(HUB))
                        a["outils"].append(float(np.mean(outil)) if lst else 0.0)
                        a["vide"] += int(len(lst) == 0)
                ligne = {"n": n, "m": m, "f": round(m / n, 4), "k_outils": k, "remedes": {}}
                for nom, a in acc.items():
                    if nom.startswith("cout_"):
                        ligne[nom] = float(np.mean(a))
                    else:
                        ligne["remedes"][nom] = {"retention_pivot": 1 - a["pivot"] / GRAINES,
                                                 "pont_du_pivot_bloque": a["pont_bloque"] / GRAINES,
                                                 "repulsion_hub": a["hub"] / GRAINES,
                                                 "part_mots_outils_dans_liste": float(np.mean(a["outils"])),
                                                 "liste_vide": a["vide"] / GRAINES}
                res.append(ligne)
                print("remèdes", n, m, k, "fait")
    return res


def partie_cout():
    res = []
    for longueur in (30, 60, 120, 240):
        for m in (1, 2, 4, 8, 12, 16, 20):
            rng = cm.generateur("b3_cout", longueur, m)
            vocab = tx.pseudo_mots(rng, 800, {"magnesium"})
            textes, _, _ = tx.corpus_ponts(rng, 20, m, 12, pivot="magnesium", vocab=vocab, taille_vocab=400,
                                           longueur=longueur)
            docs = [tx.jetons(x) for x in textes]
            voisins = tx.graphe_cooccurrence(docs)
            d_b = len(voisins.get("magnesium", ()))
            t0 = time.perf_counter()
            explicite = tx.aretes_graphe_de_ligne_par(voisins, "magnesium", explicite=True)
            duree = time.perf_counter() - t0
            bg_in, bg_out = set(), set()
            for d in docs:
                for a, b in zip(d[:-1], d[1:]):
                    if b == "magnesium":
                        bg_in.add(a)
                    if a == "magnesium":
                        bg_out.add(b)
            somme = sum(len(v) * (len(v) - 1) // 2 for v in voisins.values())
            res.append({"longueur": longueur, "m": m, "d_B": d_b, "aretes_ligne_par_B_explicite": explicite,
                        "C_dB_2": d_b * (d_b - 1) // 2, "egalite": explicite == d_b * (d_b - 1) // 2,
                        "duree_enumeration_s": duree, "noeuds_G": len(voisins),
                        "aretes_G": sum(len(v) for v in voisins.values()) // 2,
                        "aretes_graphe_de_ligne_total": somme,
                        "bigramme_entrees_x_sorties_B": len(bg_in) * len(bg_out)})
    pts = [(r["d_B"], r["aretes_ligne_par_B_explicite"]) for r in res if r["d_B"] >= 10]
    x = np.log([p[0] for p in pts])
    y = np.log([p[1] for p in pts])
    pente = float(np.polyfit(x, y, 1)[0])
    return {"points": res, "pente_log_log_aretes_vs_dB": pente, "points_ajustes": len(pts)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--heure", required=True)
    args = ap.parse_args()
    t0 = time.time()
    capacite, emp_cap = cm.capacite_organisme()
    seuil = partie_seuil(capacite)
    print("seuil fait", round(time.time() - t0, 1))
    remedes = partie_remedes(capacite)
    print("remèdes faits", round(time.time() - t0, 1))
    cout = partie_cout()
    sortie = {
        "essai": "brique 3, essai 4 : corpus synthétiques de ponts",
        "heure_lancement_utc": args.heure,
        "duree_s": round(time.time() - t0, 1),
        "graines": cm.description_graines() | {"taches": {"b3_seuil": "(5, n, m, k, id_pivot, s) ; vocabulaire (5, 999, s)",
                                                          "b3_remedes": "(6, n, m, k, s) ; fond (6, 777, s)",
                                                          "b3_cout": "(7, longueur, m)"}},
        "versions": cm.versions(),
        "instrument": {"fonction": "calculer_capacite_shannon_gram (copie exacte)", "empreinte_segment": emp_cap},
        "parametres": {"graines": GRAINES, "n": TAILLES_N, "k_outils": K_OUTILS, "pivots": PIVOTS, "hub": HUB,
                       "texte": "60 mots de domaine (Zipf s = 1,1 sur 60) + k mots-outils fixes + 20 mots-outils à 0,5",
                       "remede_b": "rho = 0,25 ; contraste = 1 - sim_inter / sim_intra ; tau dans {0,5 ; 0,7 ; 0,9}",
                       "remede_b_plus": "tau = 0,7 et fréquence de fond <= 0,1 (fond : 300 textes, hub 0,8, pivot 0,01)"},
        "seuil": seuil,
        "remedes": remedes,
        "cout_graphe_de_ligne": cout,
    }
    cm.ecrire_json(cm.SORTIE / "resultats-b3-synthetique-v1.json", sortie)
    print("fini", sortie["duree_s"], "s")


if __name__ == "__main__":
    main()
