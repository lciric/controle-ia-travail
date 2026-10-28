"""Brique 3, essai 4 (cas réel) : termes saturés de la question ouverte gen18, reconstruits depuis le rapport.

Textes des 5 castes = « Contribution » du rapport (+ la ligne JSON de vote pour les castes 2 à 5, que
_parser_contribution_question_ouverte a retirée du corps). Validation : la copie exacte de
calculer_capacite_shannon_gram doit redonner capacité, gain, similarité et termes saturés du rapport.
Usage : python3 -I -B essai_b3_gen18_v1.py --heure "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
"""
import argparse
import ast
import json
import re
import sys
import time
from collections import Counter
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))
import commun_v1 as cm
import textes_v1 as tx

ATTENDU = {"capacite_shannon": 3.618972, "gain_marginal": 0.723794, "similarite_moyenne": 0.305903,
           "termes_satures": ["article", "aux", "bruit", "cholesky", "confiance", "dans"]}


def reconstruire():
    texte = cm.lire_fourni("rapport-meta-conception.md").decode("utf-8").replace("\r\n", "\n")
    lignes = texte.split("\n")
    idx = [i for i, l in enumerate(lignes) if l.startswith("### Caste #")]
    fin = next(i for i, l in enumerate(lignes) if l.startswith("## 4. Ce dont l'essaim n'est pas sûr"))
    corps = []
    for a, i in enumerate(idx):
        j = idx[a + 1] if a + 1 < len(idx) else fin
        k = next(t for t in range(i, j) if lignes[t] == "- **Contribution** :")
        bloc = lignes[k + 2:j]
        while bloc and bloc[-1] == "":
            bloc.pop()
        corps.append("\n".join(bloc))
    votes = []
    for l in lignes:
        m = re.search(r'confiance=`([0-9.]+)` \| poids_vote=`[0-9.]+` \| vote="(.*)" \| incertitude="(.*)"$', l)
        if l.startswith("  * Caste #") and m:
            votes.append({"position": m.group(2), "confiance": float(m.group(1)), "incertitude": m.group(3)})
    textes = [c if a == 0 else c + "\n" + json.dumps(votes[a], ensure_ascii=False) for a, c in enumerate(corps)]
    debut_q = next(i for i, l in enumerate(lignes) if l.startswith("## Question posée"))
    fin_q = next(i for i, l in enumerate(lignes) if l.startswith("## 1. Réponse finale"))
    question = "\n".join(lignes[debut_q + 1:fin_q])
    return textes, question


def gabarit_consigne():
    """Chaînes littérales des consignes envoyées aux castes (prompt_c, prompt_syn, bloc_anterieur)."""
    source = cm.lire_fourni("organisme/principal.py").decode("utf-8")
    arbre = ast.parse(source)
    fn = next(n for n in arbre.body if isinstance(n, ast.FunctionDef) and n.name == "_traiter_question_ouverte")
    morceaux = []
    for noeud in ast.walk(fn):
        if isinstance(noeud, ast.Assign) and any(isinstance(t, ast.Name) and t.id in ("prompt_c", "prompt_syn", "bloc_anterieur")
                                                for t in noeud.targets):
            for sous in ast.walk(noeud.value):
                if isinstance(sous, ast.Constant) and isinstance(sous.value, str):
                    morceaux.append(sous.value)
    return "\n".join(morceaux)


def nature_fragment(tok: str, textes: list) -> str:
    """'fragment' si toutes les occurrences sont collées à une lettre non ASCII, 'mixte' si certaines, sinon 'mot'."""
    total, collees = 0, 0
    for x in textes:
        bas = x.lower()
        for m in re.finditer(r"(?<![a-z0-9_])" + re.escape(tok) + r"(?![a-z0-9_])", bas):
            total += 1
            avant = bas[m.start() - 1] if m.start() > 0 else " "
            apres = bas[m.end()] if m.end() < len(bas) else " "
            if (avant.isalpha() and not avant.isascii()) or (apres.isalpha() and not apres.isascii()):
                collees += 1
    if total == 0:
        return "absent"
    return "fragment" if collees == total else ("mixte" if collees else "mot")


def classer(tok, jq, jg, textes):
    return {"jeton": tok, "mot_outil_ou_nombre": tx.est_arret(tok), "dans_question": tok in jq,
            "dans_gabarit_consigne": tok in jg, "forme": nature_fragment(tok, textes)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--heure", required=True)
    args = ap.parse_args()
    t0 = time.time()
    capacite, emp_cap = cm.capacite_organisme()
    textes, question = reconstruire()
    jq = set(tx.jetons(question))
    jg = set(tx.jetons(gabarit_consigne()))
    res = capacite(textes)
    valide = all(abs(res[k] - ATTENDU[k]) < 5e-7 for k in ("capacite_shannon", "gain_marginal", "similarite_moyenne")) \
        and res["termes_satures"] == ATTENDU["termes_satures"]

    docs = [tx.jetons(x) for x in textes]
    df = tx.frequences_document(docs)
    n = len(docs)
    par_df = Counter(df.values())
    df5 = sorted(t for t, c in df.items() if c == n)
    cands = sorted([(t, c) for t, c in df.items() if c >= tx.seuil_saturation(n)], key=lambda kv: (-kv[1], kv[0]))
    classes_df5 = [classer(t, jq, jg, textes) for t in df5]
    resume_df5 = Counter()
    for c in classes_df5:
        if c["mot_outil_ou_nombre"]:
            resume_df5["mot_outil_ou_nombre"] += 1
        elif c["forme"] == "fragment":
            resume_df5["fragment_accent"] += 1
        elif c["dans_gabarit_consigne"]:
            resume_df5["gabarit_consigne"] += 1
        elif c["dans_question"]:
            resume_df5["question"] += 1
        else:
            resume_df5["autre_contenu"] += 1
    injectees = {}
    for k in (2, 3, 4):
        lst = capacite(textes[:k])["termes_satures"]
        injectees[f"{k}_textes"] = {"liste": lst, "classes": [classer(t, jq, jg, textes[:k]) for t in lst]}

    rem_a = tx.remede_a(textes, capacite)
    rem_b = tx.remede_b(textes)
    docs_arret = [[t for t in d if not tx.est_arret(t)] for d in docs]
    x_arret = tx._tfidf(docs_arret, set())
    import itertools
    import numpy as np
    nuls = []
    for taille in (2, 3):
        for grp in itertools.combinations(range(n), taille):
            g_arr = np.array([1 if i in grp else 0 for i in range(n)])
            nuls.append(tx.contraste_groupes(x_arret, g_arr))
    contraste_nul = {"bipartitions": len(nuls), "min": float(min(nuls)), "max": float(max(nuls)),
                     "moyenne": float(np.mean(nuls))}
    rem_c = {f"{mode}_{'arret' if arret else 'brut'}": tx.remede_c(textes, mode, arret)
             for mode in ("cooccurrence", "bigramme") for arret in (False, True)}
    for v in rem_c.values():
        v["paires_saturees"] = [list(p) for p in v["paires_saturees"]]
    voisins = tx.graphe_cooccurrence(docs)
    degres = {t: len(v) for t, v in voisins.items()}
    somme_cd2 = sum(d * (d - 1) // 2 for d in degres.values())
    aretes_g = sum(degres.values()) // 2
    sat_degres = {t: {"degre": degres.get(t, 0), "aretes_graphe_de_ligne": degres.get(t, 0) * (degres.get(t, 0) - 1) // 2}
                  for t in ATTENDU["termes_satures"]}

    sortie = {
        "essai": "brique 3, essai 4 : cas réel gen18",
        "heure_lancement_utc": args.heure,
        "duree_s": round(time.time() - t0, 2),
        "versions": cm.versions(),
        "instrument": {"fonction": "calculer_capacite_shannon_gram (copie exacte)", "empreinte_segment": emp_cap},
        "reconstruction": {"textes": n, "longueurs_jetons": [len(d) for d in docs], "resultat": res,
                           "attendu_rapport": ATTENDU, "reproduction_exacte": valide},
        "frequences_documentaires": {"seuil": tx.seuil_saturation(n), "nb_jetons_par_df": dict(sorted(par_df.items())),
                                     "nb_candidats_satures": len(cands), "jetons_df_5": df5,
                                     "rang_coupure_plafond_6": [t for t, _ in cands[:6]],
                                     "classes_jetons_df_5": classes_df5, "resume_classes_df_5": dict(resume_df5)},
        "termes_satures_rapport_classes": [classer(t, jq, jg, textes) for t in ATTENDU["termes_satures"]],
        "listes_reellement_injectees": {"note": "caste 3 reçoit la liste calculée sur 2 textes, caste 4 sur 3 textes ; "
                                                "caste 2 (1 texte) reçoit une liste vide ; l'arbitre n'en reçoit pas ; "
                                                "la liste du rapport (5 textes) est calculée après la boucle",
                                        **injectees},
        "remedes_sur_textes_reels": {"a_liste_arret": rem_a,
                                     "b_exemption_ponts": {"termes_satures": rem_b["termes_satures"], "exemptes": rem_b["exemptes"],
                                                           "contraste_global": rem_b["contraste_global"],
                                                           "contraste_candidats_min_max": [min(rem_b["contrastes_candidats"].values()),
                                                                                           max(rem_b["contrastes_candidats"].values())],
                                                           "groupes": rem_b["groupes"],
                                                           "contraste_toutes_bipartitions_reference": contraste_nul},
                                     "c_paires": rem_c},
        "graphe_cooccurrence_reel": {"noeuds": len(degres), "aretes": aretes_g, "degre_max": max(degres.values()),
                                     "aretes_graphe_de_ligne_somme_C_d_2": somme_cd2,
                                     "termes_satures_degre": sat_degres},
    }
    cm.ecrire_json(cm.SORTIE / "resultats-b3-gen18-v1.json", sortie)
    print("reproduction exacte :", valide, "|", res)


if __name__ == "__main__":
    main()
