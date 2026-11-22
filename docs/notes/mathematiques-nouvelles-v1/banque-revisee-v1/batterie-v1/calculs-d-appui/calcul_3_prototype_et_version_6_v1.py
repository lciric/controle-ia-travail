"""Calcul d'appui 3 du concepteur — deux contrôles de la batterie de fuite (prototype) — v1.

Calcul d'appui, non vérifié : il éprouve le texte de la batterie ; ce n'est pas l'instrument.

Partie A. La sonde numérique PROTOTYPE du diagnostic (15 traits communs à tous les gabarits, une seule régression,
apprise dans la racine sur neuf mondes ; script `diagnostic-fuite-v6-opus-v1.py`, ea853af4…, fonctions importées sans
changement) est appliquée aux banques d'épreuve « saine » et « grandeur » (dose 1) du calcul 2. Question : voit-elle
une vérité portée par la grandeur du littéral quand le sens change d'un squelette à l'autre ?

Partie B. La batterie (prototype du calcul 2) est appliquée à la banque de la VERSION 6 du générateur, sur ses 41
racines d'essai déjà exposées (0 à 39 et 20261122 ; aucune racine neuve, aucune banque réelle). Attendu : C1 à C4
tombent toutes ; l'aire qui fait foi et la part de la règle aveugle retrouvent les nombres du diagnostic
(moyennes 0,966 et 0,846). En description : la règle des instances saillantes et la règle de trois instances au
hasard (probabilité exacte, d'après le profil complet des instances jusqu'à 3N).

Emploi (depuis ce dossier) :
  PYTHONPATH=<dépôt>/src python3 calcul_3_prototype_et_version_6_v1.py \
      ../../diagnostic-opus-v1/diagnostic-fuite-v6-opus-v1.py SORTIE.json > SORTIE.txt
"""
from __future__ import annotations

import importlib.util
import json
import sys
import time
from fractions import Fraction

import numpy as np

from controle_ia.oracles_plantes_v6 import banque as pk_banque
from controle_ia.oracles_plantes_v6 import parametres as pk_parametres
from controle_ia.oracles_plantes_v6.forme_seule import mesurer
from controle_ia.oracles_plantes_v6.graines import generateur
from controle_ia.oracles_plantes_v6.sous_banque import identifiants_opaques, tirer_sous_banque

import calcul_2_banc_d_epreuve_v1 as banc
from outils_batterie_v1 import rappel_bloc_entier
from sondes_batterie_v1 import (FT, PG, PLIS, V, aire_qui_fait_foi, ecarts_C1, exces_par_ensemble, juger, plis_des_mondes,
                                regle_aveugle_A, scores_de_style, scores_des_nombres, squelette, trois_instances_au_hasard)

T0 = time.time()


def journal(msg):
    print(f"[{time.time() - T0:7.1f} s] {msg}", file=sys.stderr, flush=True)


def charger_diagnostic(chemin):
    spec = importlib.util.spec_from_file_location("diagnostic_opus", chemin)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def partie_A(diag, cap):
    """Sonde prototype : traits_numeriques(texte, monde) et Logistique du diagnostic ; plis par mondes entiers dans la
    racine ; apprise sur le vivier des mondes d'apprentissage, notée sur la sous-banque."""
    sortie = []
    for variante, dose in (("saine", 0.0), ("grandeur", 1.0)):
        lignes = []
        for r in banc.RACINES:
            mondes, vivier, sb = banc.construire(r, variante, dose, cap)
            pli = plis_des_mondes(r, len(mondes))
            scores = {}
            for k in range(PLIS):
                app = [x for x in vivier if pli[x["w"]] != k]
                test = [x for x in vivier if pli[x["w"]] == k]
                m = diag.Logistique([diag.traits_numeriques(x["texte"], mondes[x["w"]]) for x in app], [int(x["y"]) for x in app])
                for x, s in zip(test, m.score([diag.traits_numeriques(x["texte"], mondes[x["w"]]) for x in test])):
                    scores[x["cle"]] = s
            lignes.append(exces_par_ensemble(sb, scores))
        d = {"variante": variante, "dose": dose}
        for j, ens in enumerate(("faux_tot", "pieges", "tous_les_faux")):
            d[ens] = juger([l[ens] for l in lignes], 0.10, 2030 + j)
        sortie.append(d)
        journal(f"partie A : {variante} faite")
    return sortie


def nombres_servis(m) -> list:
    """Tous les nombres de la définition servie d'un monde : borne N, paramètres, constantes."""
    out = [Fraction(m.N)]

    def lire(x):
        if isinstance(x, (list, tuple)):
            for y in x:
                lire(y)
        elif isinstance(x, dict):
            for y in x.values():
                lire(y)
        elif isinstance(x, bool):
            return
        elif isinstance(x, int):
            out.append(Fraction(x))
        elif isinstance(x, Fraction):
            out.append(x)
        elif isinstance(x, str):
            s = x.strip().strip("()")
            try:
                out.append(Fraction(s))
            except (ValueError, ZeroDivisionError):
                pass
    lire(m.parametres_servis())
    lire(dict(m.constantes()))
    return out


def partie_B(params, diag):
    racines = list(range(40)) + [20261122]
    par_racine, lignes = {}, []
    for r in racines:
        B = pk_banque.construire_banque(r, params)
        mondes = [m for m, _ in B]
        ids = identifiants_opaques(generateur(r, 3, 0), len(B), "monde-")
        servie, cle_sb = tirer_sous_banque(B, ids, r, params["sous_banque"])
        vivier = []
        for w, (m, plantes) in enumerate(B):
            sv = nombres_servis(m)
            for p in plantes:
                if p.etiquette in (V, FT, PG):
                    vivier.append({"cle": (w, p.gabarit), "w": w, "texte": p.texte, "etiquette": p.etiquette,
                                   "y": p.etiquette != V, "paire": None, "N": m.N, "servis": sv, "gabarit": p.gabarit,
                                   "monde_id": m.empreinte_monde()})
        par_cle = {(ids[x["w"]], x["etiquette"], x["gabarit"]): x for x in vivier}
        sb = [par_cle[(c["identifiant_monde"], c["etiquette"], c["gabarit"])] for c in cle_sb["items"] if c["role"] == "analyse"]
        sc_style, vus = scores_de_style(vivier, r, len(B))
        foi = aire_qui_fait_foi(vivier, sc_style, vus)
        foi_paquet = Fraction(mesurer(B, generateur(r, 10, 0), PLIS, Fraction(1))["classifieur_de_style"]["aire_qui_fait_foi"])
        faux = [x for x in sb if x["y"]]
        vA = sum(regle_aveugle_A(mondes[x["w"]], x["texte"]) for x in faux) / len(faux)
        # description : instances saillantes et trois instances au hasard (fonctions du diagnostic, inchangées)
        saill, hasard = [], []
        for x in faux:
            m = mondes[x["w"]]
            arbre = m.analyser(x["texte"])
            saill.append(any(diag.touche(m, arbre, diag.instance_uniforme(m, arbre, v)) for v in diag.valeurs_saillantes(m, x["texte"])))
            pr = diag.profil_instances(m, arbre)
            hasard.append(None if pr.get("hors_capacite") else trois_instances_au_hasard(pr["n_instances"], pr["n_fausses"]))
        lignes.append({"racine": r, "ecarts_C1": len(ecarts_C1(vivier, sb)), "aire_qui_fait_foi": float(foi),
                       "v_saillantes": float(np.mean(saill)),
                       "v_hasard": None if any(h is None for h in hasard) else float(np.mean(hasard)),
                       "foi_egale_au_paquet": foi == foi_paquet, "style": exces_par_ensemble(sb, sc_style),
                       "style_bloc": exces_par_ensemble(sb, sc_style, rappel_bloc_entier), "v_A": vA, "touches_A": round(vA * len(faux)),
                       "sb": sb, "squelettes": len({squelette(x["texte"]) for x in vivier})})
        par_racine[r] = vivier
        journal(f"partie B : racine {r} faite (foi {float(foi):.4f}, A {round(vA * len(faux))}/75)")
    sc_num, neutres = scores_des_nombres(par_racine)
    for l in lignes:
        l["nombres"] = exces_par_ensemble(l["sb"], sc_num[l["racine"]])
        del l["sb"]
    res = {"racines": racines,
           "C1": {"racines_avec_ecart": sum(1 for l in lignes if l["ecarts_C1"]), "tenue": all(l["ecarts_C1"] == 0 for l in lignes)},
           "C2": juger([l["aire_qui_fait_foi"] for l in lignes], 0.75, 2000),
           "aire_identique_au_paquet_sur_toutes_les_racines": all(l["foi_egale_au_paquet"] for l in lignes),
           "C3": {}, "C4": juger([l["v_A"] for l in lignes], 0.50, 2010),
           "description": {"instances_saillantes": juger([l["v_saillantes"] for l in lignes], 0.50, 2040),
                           "trois_instances_au_hasard": juger([l["v_hasard"] for l in lignes], 0.50, 2041),
                           "enonces_notes_a_zero_faute_d_apprentissage": neutres},
           "touches_de_la_regle_aveugle_sur_75": {"min": min(l["touches_A"] for l in lignes), "mediane": float(np.median([l["touches_A"] for l in lignes])),
                                                   "max": max(l["touches_A"] for l in lignes)},
           "squelettes_distincts_par_racine": {"min": min(l["squelettes"] for l in lignes), "max": max(l["squelettes"] for l in lignes)}}
    for sonde, j0 in (("style", 1), ("nombres", 4), ("style_bloc", 11)):
        for k, ens in enumerate(("faux_tot", "pieges", "tous_les_faux")):
            res["C3"][f"{sonde}/{ens}"] = juger([l[sonde][ens] for l in lignes], 0.10, 2000 + j0 + k)
    res["lignes"] = lignes
    return res


def main(chemin_diag, chemin_json):
    params, sha = pk_parametres.charger()
    diag = charger_diagnostic(chemin_diag)
    out = {"numpy": np.__version__, "parametres_sha256": sha, "partie_A_sonde_prototype_sur_le_banc": partie_A(diag, params["capacites"]),
           "partie_B_batterie_sur_la_version_6": partie_B(params, diag)}
    with open(chemin_json, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1, sort_keys=True)
        fh.write("\n")
    print("Calcul d'appui 3 — sonde prototype sur le banc ; batterie sur la version 6")
    print("\nA. Sonde numérique prototype du diagnostic (traits communs, apprise dans la racine), 120 racines d'épreuve")
    for d in out["partie_A_sonde_prototype_sur_le_banc"]:
        print(f"  banque « {d['variante']} », dose {d['dose']}")
        for ens in ("faux_tot", "pieges", "tous_les_faux"):
            print(f"    excès {ens:14s} : {d[ens]}")
    b = out["partie_B_batterie_sur_la_version_6"]
    print("\nB. Batterie sur la version 6 (41 racines d'essai déjà exposées)")
    print(f"  C1 : tenue {b['C1']['tenue']} ; racines avec écart {b['C1']['racines_avec_ecart']} sur 41")
    print(f"  C2 : {b['C2']} ; aire identique à celle du paquet sur toutes les racines : {b['aire_identique_au_paquet_sur_toutes_les_racines']}")
    for k, v in b["C3"].items():
        print(f"  C3 {k:26s} : {v}")
    print(f"  C4 : {b['C4']} ; touches sur 75 : {b['touches_de_la_regle_aveugle_sur_75']}")
    print(f"  description, instances saillantes (part des 75 faux) : {b['description']['instances_saillantes']}")
    print(f"  description, trois instances au hasard (probabilité exacte) : {b['description']['trois_instances_au_hasard']}")
    print(f"  énoncés notés à zéro faute d'apprentissage (sonde des nombres) : {b['description']['enonces_notes_a_zero_faute_d_apprentissage']}")
    print(f"  squelettes distincts par racine : {b['squelettes_distincts_par_racine']}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
