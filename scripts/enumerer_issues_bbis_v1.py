"""Énumération des grilles de lecture de l'étape B bis (`prereg/T0.7-etape-B-bis-v1.md`, « Critères de lecture gelés »,
« Exhaustivité »), v1.

Pour chaque grille, chaque combinaison d'états est classée deux fois : par des **prédicats exclusifs** écrits ici d'après le
texte (une ligne par condition, sans « première ligne qui s'applique »), et par le code de lecture (`t07bbis.lecture_v1`,
`t07bbis.conjointe_v1`) ; l'essai exige exactement une ligne vraie par combinaison (0 trou, 0 chevauchement) et l'accord des
deux classements.

- A : toutes les combinaisons des issues des épreuves d'une cellule ((ii) : 4 374 ; (i-a) : 486) ;
- B : 8⁴ vecteurs d'états du plafond de (ii) × 8⁴ vecteurs du transfert (16 777 216 paires, comptées par produit des deux
  classements, chacun exhaustif) ; les 7 × 4 = 28 paires (I, suffixe), une phrase par paire ; libellés du nœud 5 sur 8⁴ × 3⁴
  qualifications de MU (le libellé retenu implique le libellé d'information) ;
- C : 3 états de B × les 16 sous-ensembles de doses jugées × les états (et qualifications de MU) de ces doses, pour les deux
  variantes ; (i-a) : 3 × 6.

Usage : `PYTHONPATH=src python scripts/enumerer_issues_bbis_v1.py [--sortie FICHIER.json]`. Aucune donnée lue.
"""
from __future__ import annotations

import argparse
import itertools
import json
import sys
from collections import Counter

from controle_ia.t07bbis import conjointe_v1 as cj
from controle_ia.t07bbis import lecture_v1 as lv

DOSES = ("S25", "S50", "S75", "S100")
ETATS = lv.ETATS
MUS = (lv.MU_MUETTE, lv.MU_ALLUMEE, lv.MU_NC)
R = {"E1": 1, "E1b": 1, "E2": 2, "E3": 3, "E4": 4, "E5": 5, "E6": 6}


# --------------------------------------------------------------------------------------------------------------- grille A

def _ligne(etat):
    if etat == "nc":
        return {"non_calculable": "essai"}
    return {"au_dessus": etat == "oui", "passe": etat == "oui", "aire": 0.8, "Q": 0.6, "difference": 0.1, "bas": 0.01, "haut": 0.2}


def grille_a(famille: str) -> dict:
    tri = ("nc", "non", "oui")
    axes = [tri, tri, (False, True), tri, tri, tri] + ([tri, tri] if famille == "(ii)" else [])
    compte, accords, lignes = 0, 0, Counter()
    for combo in itertools.product(*axes):
        D, Rr, triv, mc, lex, enc = combo[:6]
        te, dd = (combo[6], combo[7]) if famille == "(ii)" else (None, None)
        calc = D != "nc" and Rr != "nc"
        lect = all(x == "oui" for x in (mc, lex, enc))
        preds = {
            "E0": not calc,
            "E1": calc and D == "non",
            "E1b": calc and D == "oui" and Rr == "non",
            "E2": calc and D == "oui" and Rr == "oui" and triv,
            "E3": calc and D == "oui" and Rr == "oui" and not triv and not lect,
        }
        if famille == "(ii)":
            preds.update({"E4": calc and D == "oui" and Rr == "oui" and not triv and lect and te != "oui",
                          "E5": calc and D == "oui" and Rr == "oui" and not triv and lect and te == "oui" and dd != "oui",
                          "E6": calc and D == "oui" and Rr == "oui" and not triv and lect and te == "oui" and dd == "oui"})
        else:
            preds["E6′"] = calc and D == "oui" and Rr == "oui" and not triv and lect
        vraies = [k for k, v in preds.items() if v]
        if len(vraies) != 1:
            raise SystemExit(f"grille A {famille} : {combo} → {vraies} (trou ou chevauchement)")
        r = {"famille": famille, "D": _ligne(D), "R": _ligne(Rr), "MC": _ligne(mc), "LEX": _ligne(lex), "ENC": _ligne(enc),
             "triviaux": {"t": {"separation": 0.9 if triv else 0.5}}}
        if D == "oui":
            r["D"]["aire"] = 0.8
        if famille == "(ii)":
            r["TE"], r["DD"] = _ligne(te), _ligne(dd)
        e = lv.etat_cellule(r)["etat"]
        accords += int(e == vraies[0])
        compte += 1
        lignes[vraies[0]] += 1
    if accords != compte:
        raise SystemExit(f"grille A {famille} : {compte - accords} désaccords entre prédicats et code")
    return {"combinaisons": compte, "trous": 0, "chevauchements": 0, "par_etat": dict(lignes)}


# --------------------------------------------------------------------------------------------------------------- grille B

def _pred_issue(v) -> list:
    non_e0 = [e for e in v if e != "E0"]
    h = max((R[e] for e in non_e0), default=0)
    return [k for k, ok in (("I0", not non_e0), ("I1", bool(non_e0) and h == 1), ("I2", h == 2), ("I3", h == 3),
                            ("I4", h == 4), ("I5", h == 5), ("I6", h == 6)) if ok]


def _pred_suffixe(v) -> list:
    non_e0 = [e for e in v if e != "E0"]
    h = max((R[e] for e in non_e0), default=0)
    return [k for k, ok in (("T0", not non_e0), ("T−", bool(non_e0) and h <= 2), ("T±", 3 <= h <= 5), ("T+", h == 6)) if ok]


def grille_b() -> dict:
    ci, ct = Counter(), Counter()
    for v in itertools.product(ETATS, repeat=4):
        pi, pt = _pred_issue(v), _pred_suffixe(v)
        if len(pi) != 1 or len(pt) != 1:
            raise SystemExit(f"grille B : {v} → {pi}, {pt}")
        e = dict(zip(DOSES, v))
        if lv.issue_code(e)[0] != pi[0] or lv.suffixe_code(e)[0] != pt[0]:
            raise SystemExit(f"grille B : désaccord sur {v}")
        ci[pi[0]] += 1
        ct[pt[0]] += 1
    paires = Counter({(i, t): ci[i] * ct[t] for i in ci for t in ct})
    total = sum(paires.values())
    if total != 8 ** 8 or len(paires) != 28:
        raise SystemExit(f"grille B : {total} paires, {len(paires)} classes")
    lib, implique = Counter(), 0
    for v in itertools.product(ETATS, repeat=4):
        e = dict(zip(DOSES, v))
        for mu in itertools.product(MUS, repeat=4):
            m = dict(zip(DOSES, mu))
            dure = any(e[d] == "E6" and m[d] == lv.MU_MUETTE for d in DOSES)
            lettre = any(e[d] in ("E5", "E6") for d in DOSES)
            l = lv.libelles(e, m)
            if l["lecture_dure"]["oui"] != dure or l["lettre_R2716"]["oui"] != lettre:
                raise SystemExit(f"libellés : désaccord sur {v}, {mu}")
            if dure and not lettre:
                raise SystemExit("libellés : le libellé retenu sans le libellé d'information")
            implique += int(dure <= lettre)
            lib[(dure, lettre)] += 1
    return {"vecteurs_plafond": 8 ** 4, "vecteurs_transfert": 8 ** 4, "paires": total, "classes_I_suffixe": 28,
            "par_issue": dict(ci), "par_suffixe": dict(ct),
            "libelles": {"combinaisons": sum(lib.values()), "dure_et_lettre": lib[(True, True)], "lettre_seule": lib[(False, True)],
                         "aucun": lib[(False, False)], "dure_sans_lettre": lib[(True, False)]}}


def phrases_28() -> list:
    """Une phrase par paire (I, suffixe), sur des cellules d'essai qui atteignent chaque état."""
    def cellule(etat):
        c = {"etat": {"etat": etat, "nom": "jetons_notes", "lecteur": "MC", "motif": None},
             "D": {"aire": 0.62, "bas_echelle_aire": 0.55, "haut_echelle_aire": 0.7, "Q": 0.6},
             "MC": {"difference": 0.01, "bas": -0.02, "haut": 0.04},
             "TE": {"aire": 0.58, "bas_echelle_aire": 0.5, "haut_echelle_aire": 0.66, "Q": 0.6},
             "ART": {"aire": 0.53, "deplacement": False}, "DD": {"difference": 0.05, "bas": 0.01, "haut": 0.09}}
        return c
    sortie = []
    exemples_i = {"I0": "E0", "I1": "E1", "I2": "E2", "I3": "E3", "I4": "E4", "I5": "E5", "I6": "E6"}
    exemples_t = {"T0": "E0", "T−": "E1", "T±": "E4", "T+": "E6"}
    for i, ei in exemples_i.items():
        for t, et in exemples_t.items():
            pl = {d: cellule(ei) for d in DOSES}
            tr = {d: cellule(et) for d in DOSES}
            code, doses = lv.issue_code({d: ei for d in DOSES})
            tc, td = lv.suffixe_code({d: et for d in DOSES})
            if (code, tc) != (i, t):
                raise SystemExit(f"phrases : {i}, {t} non atteintes")
            sortie.append({"I": i, "T": t, "phrase": lv.phrase_issue(code, doses, pl) + " " + lv.phrase_suffixe(tc, td, tr) + " "
                           + lv.PHRASE_MODE})
    return sortie


# --------------------------------------------------------------------------------------------------------------- grille C

def _pred_p(etats, mus, jugees, variante) -> list:
    tient = lambda d: (etats[d] == "E6" and mus[d] == lv.MU_MUETTE) if variante == cj.RETENUE else etats[d] in ("E5", "E6")
    moins = any(etats[d] in ("E1", "E1b", "E2") for d in jugees)
    zero = (not jugees) or any(etats[d] == "E0" for d in jugees)
    plus = bool(jugees) and all(tient(d) for d in jugees)
    return [k for k, ok in (("P−", moins), ("P0", not moins and zero), ("P+", not moins and not zero and plus),
                            ("P±", not moins and not zero and not plus)) if ok]


def _pred_c(b, p) -> list:
    return [k for k, ok in (("C0", b == "B0" or p == "P0"), ("C1", b == "B+" and p == "P+"), ("C2", b == "B+" and p == "P±"),
                            ("C3", b == "B+" and p == "P−"), ("C4", b == "B−" and p == "P+"), ("C5", b == "B−" and p == "P±"),
                            ("C6", b == "B−" and p == "P−")) if ok]


def grille_c() -> dict:
    comptes = {cj.RETENUE: Counter(), cj.INFORMATION: Counter()}
    n = 0
    for b_entree in ("U", "Z", None):
        b = cj.etat_b(b_entree)
        for k in range(5):
            for jugees in itertools.combinations(DOSES, k):
                for v in itertools.product(ETATS, repeat=k):
                    for mu in itertools.product(MUS, repeat=k):
                        etats, mus = dict(zip(jugees, v)), dict(zip(jugees, mu))
                        for variante in (cj.RETENUE, cj.INFORMATION):
                            pp = _pred_p(etats, mus, list(jugees), variante)
                            if len(pp) != 1:
                                raise SystemExit(f"grille C : P {pp} pour {etats}, {mus}")
                            pc = _pred_c(b, pp[0])
                            if len(pc) != 1:
                                raise SystemExit(f"grille C : C {pc}")
                            p_code, _ = cj.etat_bbis_ii(etats, mus, list(jugees), variante)
                            if p_code != pp[0] or cj.ligne_c(b, p_code) != pc[0]:
                                raise SystemExit(f"grille C : désaccord sur {b}, {etats}, {mus}, {variante}")
                            comptes[variante][pc[0]] += 1
                        n += 1
    ia = Counter()
    for b_entree in ("U", "Z", None):
        for e in lv.ETATS_I:
            ia[cj.ligne_c(cj.etat_b(b_entree), cj.etat_bbis_ia(e))] += 1
    attendu = 3 * sum(len(list(itertools.combinations(DOSES, k))) * (len(ETATS) * len(MUS)) ** k for k in range(5))
    if n != attendu:
        raise SystemExit(f"grille C : {n} combinaisons, {attendu} attendues")
    return {"combinaisons_ii": n, "par_ligne": {v: dict(c) for v, c in comptes.items()}, "combinaisons_ia": 18,
            "par_ligne_ia": dict(ia), "trous": 0, "chevauchements": 0}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--sortie", default=None)
    a = ap.parse_args(argv)
    r = {"A": {"(ii)": grille_a("(ii)"), "(i-a)": grille_a("(i-a)")}, "B": grille_b(), "C": grille_c(),
         "phrases_28": phrases_28()}
    texte = json.dumps(r, indent=1, ensure_ascii=False, sort_keys=True, default=str)
    if a.sortie:
        open(a.sortie, "w", encoding="utf-8").write(texte + "\n")
    print(f"A (ii) {r['A']['(ii)']['combinaisons']}, A (i-a) {r['A']['(i-a)']['combinaisons']}, B {r['B']['paires']} paires, "
          f"28 phrases, C {r['C']['combinaisons_ii']} + 18 : 0 trou, 0 chevauchement")
    return 0


if __name__ == "__main__":
    sys.exit(main())
