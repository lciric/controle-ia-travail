"""Calcul d'appui 4 du concepteur — banc d'épreuve de la batterie, version 3 du texte (prototype) — v2.

Calcul d'appui, non vérifié : il éprouve le texte `batterie-fuite-banque-revisee-v3.md` ; ce n'est pas l'instrument.
Il reprend le banc du calcul 2 (`calcul_2_banc_d_epreuve_v1.py`, importé sans changement : mêmes mondes, mêmes
racines d'épreuve 1000 à 1119, mêmes graines) et y ajoute ce que la contre-lecture (9718ec04…) et la mère demandent :

  A. Les banques : saine ; « grandeur » (doses 1, 0,5, 0,25) ; « relation entre littéraux » (doses 1 et 0,5 : pour une
     vérité, R = C - d, d de 1 à 5 ; construction du contre-lecteur) ; « gabarit » ; « plafond » ; « fenêtres »
     (contre-exemples denses à côté des trois instances de la règle A : l'énoncé « n < K ou n > L », en quatre
     écritures, est faux sur [K .. L], fenêtre large placée dans [2 .. N] pour un faux tôt, dans [N + 2 .. 3N - 1]
     pour un piège, vide pour une vérité) ; et deux fuites cantonnées (« grandeur » à pleine dose sur la seule
     première écriture, soit un quart des énoncés ; puis sur la première écriture des seuls mondes de borne 4, soit
     un douzième).
     Pour chacune : C1 ; C2 ; C3 (style, nombres avec Newton amorti et garde de convergence) ; C4 à deux règles (règle
     aveugle A ; règle de trois instances au hasard, probabilité exacte, avec un tirage de contrôle à graine
     consignée) ; en description, l'excès « côté vrai », l'excès par écriture, les instances saillantes.
  B. Les gardes (règle R5) : cinq banques qui violent chacune un point de C1 ; une sonde aux scores inversés (audit
     « trop beau ») ; 39 racines plantées ; un apprentissage arrêté avant convergence ; les cas « non calculable ».
  C. La table des branches (version qui fait foi), ligne par ligne.
  D. L'indépendance des racines (remarque 16) : la sonde des nombres apprise sur l'autre moitié des racines, comparée
     à la sonde apprise sur toutes les autres.

Bornes hautes : SeedSequence(20261122, spawn_key=(2000 + j,)), j = 0 (C2), 1 à 6 (C3 : style puis nombres ; faux tôt,
pièges, tous les faux), 10 (règle A), 11 (règle du hasard) ; 20 à 29 pour les mesures de description.

Emploi (depuis ce dossier ; un seul fil de calcul, pour des sorties identiques d'une passe à l'autre) :
  OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 PYTHONPATH=<dépôt>/src python3 calcul_4_banc_d_epreuve_v2.py SORTIE.json > SORTIE.txt
"""
from __future__ import annotations

import json
import sys
import time

import numpy as np

from controle_ia.oracles_plantes_v6 import parametres as pk_parametres

import calcul_2_banc_d_epreuve_v1 as banc
from outils_batterie_v1 import hors_de_la_plage
from sondes_batterie_v1 import (FT, PG, V, aire_qui_fait_foi, ecarts_C1, exces_par_ensemble, regle_aveugle_A,
                                scores_de_style, valeurs_saillantes)
from sondes_batterie_v2 import (exces_cote_vrai, exces_par_squelette, hasard_exact, hasard_tirage, juger,
                                profil_des_instances, scores_des_nombres, version_qui_fait_foi)

RACINES = banc.RACINES
T0 = time.time()


def journal(msg):
    print(f"[{time.time() - T0:7.1f} s] {msg}", file=sys.stderr, flush=True)


# ------------------------------------------------------------------------------------------------ variantes ajoutées
_tirer_v1 = banc.tirer_enonce
_GABARITS_V1 = banc.GABARITS
FENETRES = (
    ("f1", "pour tout n dans NAT, n < {K} ou n > {L}", 0),
    ("f2", "pour tout n dans NAT, n > {L} ou n < {K}", 0),
    ("f3", "pour tout n dans NAT, non (n >= {K} et n <= {L})", 0),
    ("f4", "pour tout n dans NAT, n >= {K} implique n > {L}", 0),
)


def tirer_enonce(g, gab, strate, m, variante, dose):
    """Variantes ajoutées au banc du calcul 2. Les variantes du calcul 2 passent par sa fonction, sans changement."""
    nom, forme, sens = gab
    PM, N = m.PM, m.N
    if variante == "fenetres":  # faux sur [K .. L] ; aucune des instances 3N, 1, N + 1 n'est dans une fenêtre
        if strate == FT:
            K, L = int(g.integers(2, 4)), int(g.integers(N - 1, N + 1))
        elif strate == PG:
            K, L = int(g.integers(N + 2, N + 4)), int(g.integers(3 * N - 2, 3 * N))
        else:
            L = int(g.integers(0, 3 * N + 1))
            K = L + int(g.integers(1, 4))
        return forme.format(K=K, L=L), K
    if variante == "relation":
        if strate == V and g.random() < dose:  # construction du contre-lecteur : R = C - d modulo PM
            lo, hi = banc.region(strate, N, PM, "saine")
            n0 = int(g.integers(lo, hi + 1))
            d = int(g.integers(1, 6))
            A = (-d * pow(n0, -1, PM)) % PM
            C = int(g.integers(0, PM))
            return forme.format(A=A, C=C, R=(A * n0 + C) % PM), n0
        return _tirer_v1(g, gab, strate, m, "saine", dose)
    if variante.startswith("cantonnee"):
        vise = nom == "g1" and (variante == "cantonnee_un_quart" or N == 4)
        return _tirer_v1(g, gab, strate, m, "grandeur" if vise else "saine", 1.0)
    return _tirer_v1(g, gab, strate, m, variante, dose)


banc.tirer_enonce = tirer_enonce


def construire(r, variante, dose, cap):
    banc.GABARITS = FENETRES if variante == "fenetres" else _GABARITS_V1
    try:
        return banc.construire(r, variante, dose, cap)
    finally:
        banc.GABARITS = _GABARITS_V1


def mesurer(variante, dose, cap, racines=RACINES, pas_max=None, inverser_nombres=False):
    par_racine, lignes = {}, []
    desaccords = 0
    for rang, r in enumerate(racines):
        mondes, vivier, sb = construire(r, variante, dose, cap)
        c1 = ecarts_C1(vivier, sb)
        sc_style, vus = scores_de_style(vivier, r, len(mondes))
        foi = aire_qui_fait_foi(vivier, sc_style, vus)
        faux = [x for x in sb if x["y"]]
        vA = sum(regle_aveugle_A(mondes[x["w"]], x["texte"]) for x in faux) / len(faux)
        exact, tirage, saill = [], [], []
        for k, x in enumerate(faux):
            st = profil_des_instances(mondes[x["w"]], mondes[x["w"]].analyser(x["texte"]))  # une variable : rang = n
            exact.append(hasard_exact(len(st), sum(st)))
            tirage.append(hasard_tirage(st, rang, k))
            saill.append(any(st[v] for v in valeurs_saillantes(x["texte"], x["N"])))
            premier = st.index(True) if True in st else None  # la strate plantée est celle que rend l'évaluateur exact
            desaccords += premier is None or (premier <= x["N"]) != (x["etiquette"] == FT)
        saill = float(np.mean(saill))
        lignes.append({"racine": r, "ecarts_C1": len(c1), "exemple_ecart_C1": c1[:1],
                       "aire_qui_fait_foi": None if foi is None else float(foi),
                       "style": exces_par_ensemble(sb, sc_style), "style_cote_vrai": exces_cote_vrai(sb, sc_style),
                       "v_A": vA, "v_hasard_exact": float(np.mean(exact)), "v_hasard_tirage": float(np.mean(tirage)),
                       "v_saillantes": saill, "sb": sb})
        par_racine[r] = vivier
    kw = {} if pas_max is None else {"pas_max": pas_max}
    sc_num, diag, _zeros = scores_des_nombres(par_racine, **kw)
    for l in lignes:
        s = sc_num[l["racine"]]
        if inverser_nombres and s is not None:
            s = {k: -v for k, v in s.items()}
        l["nombres"] = exces_par_ensemble(l["sb"], s) if s is not None else {e: None for e in ("faux_tot", "pieges", "tous_les_faux")}
        l["nombres_cote_vrai"] = exces_cote_vrai(l["sb"], s)
        l["nombres_par_ecriture"] = exces_par_squelette(l["sb"], s)
    res = {"variante": variante, "dose": dose, "racines": len(racines),
           "faux_dont_la_strate_differe_de_l_evaluateur_exact": int(desaccords),
           "C1": {"racines_avec_ecart": sum(1 for l in lignes if l["ecarts_C1"]), "tenue": all(l["ecarts_C1"] == 0 for l in lignes),
                  "exemple": next((l["exemple_ecart_C1"] for l in lignes if l["ecarts_C1"]), [])},
           "C2": juger([l["aire_qui_fait_foi"] for l in lignes], 0.75, 2000), "C3": {}}
    for sonde, j0 in (("style", 1), ("nombres", 4)):
        for k, ens in enumerate(("faux_tot", "pieges", "tous_les_faux")):
            res["C3"][f"{sonde}/{ens}"] = juger([l[sonde][ens] for l in lignes], 0.10, 2000 + j0 + k, plancher_d_audit=-0.03)
    res["C3"]["tenue"] = all(v["tenue"] for v in res["C3"].values())
    res["C4"] = {"regle_A": juger([l["v_A"] for l in lignes], 0.50, 2010),
                 "regle_du_hasard_exacte": juger([l["v_hasard_exact"] for l in lignes], 0.50, 2011)}
    res["C4"]["tenue"] = res["C4"]["regle_A"]["tenue"] and res["C4"]["regle_du_hasard_exacte"]["tenue"]
    ecr = sorted({k for l in lignes for k in l["nombres_par_ecriture"]})
    res["description"] = {
        "sonde_des_nombres": diag,
        "hasard_tirage_de_controle_moyenne": round(float(np.mean([l["v_hasard_tirage"] for l in lignes])), 4),
        "instances_saillantes_moyenne": round(float(np.mean([l["v_saillantes"] for l in lignes])), 4),
        "cote_vrai_style": juger([l["style_cote_vrai"] for l in lignes], 0.10, 2020),
        "cote_vrai_nombres": juger([l["nombres_cote_vrai"] for l in lignes], 0.10, 2021),
        "nombres_par_ecriture_moyenne": {e: (None if any(l["nombres_par_ecriture"].get(e) is None for l in lignes) else
                                             round(float(np.mean([l["nombres_par_ecriture"][e] for l in lignes])), 4)) for e in ecr}}
    for l in lignes:
        del l["sb"]
    res["lignes"] = lignes
    return res, par_racine


# ------------------------------------------------------------------------------------------------ B. gardes
def gardes(cap):
    out = {}
    # B1. cinq violations de C1, une par point, sur la banque saine de la racine 1000
    mondes, vivier, sb = banc.construire(1000, "saine", 0.0, cap)
    assert ecarts_C1(vivier, sb) == []

    def copie():
        v = [dict(x) for x in vivier]
        cles = {x["cle"] for x in sb}
        return v, [x for x in v if x["cle"] in cles]

    cas = {}
    v, s = copie()  # une paire à cheval sur deux mondes
    next(x for x in v if x["etiquette"] == FT)["w"] = 11
    cas["paire à cheval sur deux mondes"] = (v, s, "deux mondes")
    v, s = copie()  # une paire de squelettes différents
    x = next(x for x in v if x["etiquette"] == FT)
    x["texte"] = x["texte"].replace("pour tout n dans NAT, ", "pour tout n dans NAT, n >= 0 implique ")
    cas["paire de squelettes différents"] = (v, s, "squelettes différents")
    v, s = copie()  # une paire de textes identiques
    x = next(x for x in v if x["etiquette"] == FT)
    x["texte"] = next(y for y in v if y["paire"] == x["paire"] and y["etiquette"] == V)["texte"]
    cas["paire de textes identiques"] = (v, s, "même énoncé")
    v, s = copie()  # un squelette à deux paires à faux tôt et aucune à piège dans un monde
    next(x for x in v if x["etiquette"] == PG)["etiquette"] = FT
    cas["squelette à deux paires à faux tôt, aucune à piège"] = (v, s, "2 faux tôt, 0 pièges")
    v, s = copie()  # une sous-banque qui sert un seul membre d'une paire
    cas["sous-banque qui sert un seul membre d'une paire"] = (v, s[1:], "servie 1 fois sur 2")
    out["violations_de_C1"] = {}
    for nom, (v, s, attendu) in cas.items():
        e = ecarts_C1(v, s)
        out["violations_de_C1"][nom] = {"arretee": bool(e), "par_l_assertion_visee": any(attendu in m for m in e),
                                        "ecarts": len(e), "premier": e[0] if e else None}
    # B2. audit « trop beau » : scores de la sonde des nombres inversés sur « grandeur » à pleine dose
    res, _ = mesurer("grandeur", 1.0, cap, inverser_nombres=True)
    out["scores_inverses"] = {k: v for k, v in res["C3"].items() if k.startswith("nombres/")}
    # B3. plancher de 40 racines plantées : 39 racines
    res39, _ = mesurer("saine", 0.0, cap, racines=RACINES[:39])
    out["39_racines_plantees"] = {"C2": res39["C2"], "C3_tous_les_faux_nombres": res39["C3"]["nombres/tous_les_faux"],
                                  "C4_regle_A": res39["C4"]["regle_A"]}
    # B4. garde de convergence : un seul pas de Newton permis
    res1, _ = mesurer("saine", 0.0, cap, racines=RACINES[:40], pas_max=1)
    out["apprentissage_arrete_avant_convergence"] = {"diagnostic": res1["description"]["sonde_des_nombres"],
                                                     "C3_nombres_tous_les_faux": res1["C3"]["nombres/tous_les_faux"],
                                                     "C3_tenue": res1["C3"]["tenue"]}
    # B5. « non calculable » : un ensemble vide, un score manquant
    sans_pieges = [x for x in sb if x["etiquette"] != PG]
    sc, _ = scores_de_style(vivier, 1000, len(mondes))
    e1 = exces_par_ensemble(sans_pieges, sc)
    sc2 = dict(sc)
    sc2.pop(sb[0]["cle"])
    e2 = exces_par_ensemble(sb, sc2)
    out["non_calculable"] = {"ensemble_vide (pas de piège servi)": e1, "score_manquant": e2,
                             "jugement_avec_une_valeur_manquante": juger([0.0] * 119 + [None], 0.10, 2001)}
    # B6. relecture par la plage
    out["relecture_par_la_plage"] = {"dans_la_plage": hors_de_la_plage(0.05, [0.0, 0.1, 0.2]),
                                     "au_dessus": hors_de_la_plage(0.25, [0.0, 0.1, 0.2]),
                                     "au_dessous": hors_de_la_plage(-0.01, [0.0, 0.1, 0.2]),
                                     "non_calculable": hors_de_la_plage(None, [0.0, 0.1, 0.2])}
    return out


# ------------------------------------------------------------------------------------------------ C. branches
def branches():
    def v(nom, a_temps, c1, c2, c3, c4):
        return {"nom": nom, "a_temps": a_temps, "C1": c1, "C2": c2, "C3": c3, "C4": c4}
    cas = [
        ("version 7 : tout tient", [v("version 7", True, True, True, True, True)]),
        ("version 7 : C1 et C4 tiennent, C3 non", [v("version 7", True, True, True, False, True)]),
        ("version 7 : C4 ne tient pas", [v("version 7", True, True, True, True, False)]),
        ("version 7 : C1 ne tient pas", [v("version 7", True, False, True, True, True)]),
        ("version 7 mesurée après la date", [v("version 7", False, True, True, True, True)]),
        ("aucune version mesurée", []),
        ("version 7 : C3 non ; version 8 : tout tient", [v("version 7", True, True, True, False, True), v("version 8", True, True, True, True, True)]),
        ("version 7 : C3 non ; version 8 : C4 non", [v("version 7", True, True, True, False, True), v("version 8", True, True, True, True, False)]),
        ("version 7 : C3 non ; version 8 : C3 non", [v("version 7", True, True, True, False, True), v("version 8", True, True, False, False, True)]),
        ("version 7 : C4 non ; version 8 : C1 et C4 tiennent, C2 non", [v("version 7", True, True, True, True, False), v("version 8", True, True, False, True, True)]),
        ("version 7 : C3 non ; version 8 mesurée après la date", [v("version 7", True, True, True, False, True), v("version 8", False, True, True, True, True)]),
        ("version 7 : C4 non ; version 8 : C4 non", [v("version 7", True, True, True, True, False), v("version 8", True, True, True, True, False)]),
    ]
    return [{"cas": nom, "fait_foi": version_qui_fait_foi(m)[0], "lecture": version_qui_fait_foi(m)[1]} for nom, m in cas]


# ------------------------------------------------------------------------------------------------ D. deux moitiés
def deux_moities(par_racine_sb, par_racine_vivier, enfant):
    """Sonde des nombres apprise sur l'autre moitié des racines (rangs pairs contre rangs impairs)."""
    rangs = {r: i for i, r in enumerate(RACINES)}
    moitie = {r: {q for q in RACINES if rangs[q] % 2 != rangs[r] % 2} for r in RACINES}
    sc, diag, _ = scores_des_nombres(par_racine_vivier, apprentissage=lambda r: moitie[r])
    vals = [exces_par_ensemble(par_racine_sb[r], sc[r])["tous_les_faux"] if sc[r] is not None else None for r in RACINES]
    return juger(vals, 0.10, enfant), diag


def main(chemin):
    params, sha = pk_parametres.charger()
    cap = params["capacites"]
    plan = [("saine", 0.0), ("grandeur", 1.0), ("grandeur", 0.5), ("grandeur", 0.25), ("relation", 1.0), ("relation", 0.5),
            ("gabarit", 0.0), ("plafond", 0.0), ("fenetres", 0.0), ("cantonnee_un_quart", 1.0), ("cantonnee_un_douzieme", 1.0)]
    out = {"racines": RACINES, "numpy": np.__version__, "parametres_sha256": sha, "A_banques": [], "D_deux_moities": {}}
    for variante, dose in plan:
        res, viviers = mesurer(variante, dose, cap)
        out["A_banques"].append(res)
        journal(f"A : {variante} dose {dose} faite")
        if (variante, dose) in (("saine", 0.0), ("grandeur", 0.25), ("relation", 0.5)):
            sbs = {}
            for r in RACINES:
                _m, _v, sb = construire(r, variante, dose, cap)
                sbs[r] = sb
            j, d = deux_moities(sbs, viviers, 2025)
            out["D_deux_moities"][f"{variante}/{dose}"] = {"apprise_sur_l_autre_moitie": j, "apprise_sur_toutes_les_autres": res["C3"]["nombres/tous_les_faux"],
                                                            "diagnostic": d}
            journal(f"D : {variante} dose {dose} faite")
    out["B_gardes"] = gardes(cap)
    journal("B faite")
    out["C_branches"] = branches()
    with open(chemin, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1, sort_keys=True)
        fh.write("\n")
    print("Calcul d'appui 4 — banc d'épreuve de la batterie, version 3 du texte (prototype du concepteur)")
    print(f"120 racines d'épreuve (1000 à 1119) ; numpy {np.__version__} ; paramètres du paquet {sha[:8]}…")
    print("\nA. Banques")
    for b in out["A_banques"]:
        print(f"\n  Banque « {b['variante']} », dose {b['dose']}")
        print(f"    faux dont la strate diffère de celle de l'évaluateur exact : {b['faux_dont_la_strate_differe_de_l_evaluateur_exact']}")
        print(f"    C1 : tenue {b['C1']['tenue']} ; racines avec écart {b['C1']['racines_avec_ecart']} ; exemple {b['C1']['exemple']}")
        print(f"    C2 aire qui fait foi           : {b['C2']}")
        for k, v in b["C3"].items():
            print(f"    C3 {k:27s} : {v}")
        for k, v in b["C4"].items():
            print(f"    C4 {k:27s} : {v}")
        for k, v in b["description"].items():
            print(f"    description, {k} : {v}")
    print("\nB. Gardes")
    for k, v in out["B_gardes"].items():
        print(f"  {k}")
        for kk, vv in v.items():
            print(f"    {kk} : {vv}")
    print("\nC. Branches (version qui fait foi : la dernière version mesurée à temps qui tient C1 et C4 ; sinon la version 6)")
    for l in out["C_branches"]:
        print(f"  {l['cas']:62s} -> {l['fait_foi']} ; {l['lecture']}")
    print("\nD. Sonde des nombres apprise sur l'autre moitié des racines (excès sur tous les faux)")
    for k, v in out["D_deux_moities"].items():
        print(f"  {k}")
        for kk, vv in v.items():
            print(f"    {kk} : {vv}")


if __name__ == "__main__":
    main(sys.argv[1])
