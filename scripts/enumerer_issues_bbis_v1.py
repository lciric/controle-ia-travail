"""Énumération des grilles de lecture de l'étape B bis (`prereg/T0.7-etape-B-bis-v1.md`, « Critères de lecture gelés »,
« Exhaustivité »), v1. Aucune donnée lue.

Pour chaque grille, chaque combinaison d'états est classée deux fois : par des **prédicats exclusifs** écrits ici d'après le texte
(une condition par ligne, sans « première ligne qui s'applique »), et par le code de lecture (`t07bbis.lecture_v1`,
`t07bbis.conjointe_v1`) ; l'essai exige exactement une ligne vraie par combinaison (0 trou, 0 chevauchement) et l'accord des deux
classements.

- A : toutes les combinaisons des issues des épreuves d'une cellule (plancher, nul de réétiquetage, MC, LEX, ENC, texte égal,
  au-delà de l'artefact : chacune « non calculable », « non » ou « oui » ; prédicteur trivial : oui ou non) — (ii) : 3⁷ × 2 =
  4 374 ; (i-a) : 3⁵ × 2 = 486 ;
- B : 8⁴ vecteurs d'états du plafond de (ii) × 8⁴ vecteurs du transfert, soit 16 777 216 paires : l'issue I ne dépend que du
  vecteur du plafond et le suffixe que du vecteur du transfert ; chaque vecteur est classé (4 096 + 4 096 classements, chacun
  exhaustif et exclusif), et chaque paire reçoit la paire de classes : le décompte par paire (I, suffixe) est le produit des
  décomptes, total 8⁸ ; les 7 × 4 = 28 paires (I, suffixe) ont chacune une phrase ; libellés du nœud 5 sur 8⁴ × 3⁴ qualifications
  de MU (le libellé retenu implique le libellé d'information) ;
- C : 3 états de B × les 16 sous-ensembles de doses jugées × les états (et qualifications de MU) de ces doses, pour les deux
  variantes : 3 × (1 + 24)⁴ = 1 171 875 combinaisons ; (i-a) : 3 × 6.

Usage : `PYTHONPATH=src python scripts/enumerer_issues_bbis_v1.py [--sortie FICHIER.json]`.
"""
from __future__ import annotations

import argparse
import itertools
import json
import re
import sys
from collections import Counter

from controle_ia.t07bbis import conjointe_v1 as cj
from controle_ia.t07bbis import lecture_v1 as lv

DOSES = ("S25", "S50", "S75", "S100")
ETATS = lv.ETATS
MUS = (lv.MU_MUETTE, lv.MU_ALLUMEE, lv.MU_NC)
R = {"E1": 1, "E1b": 1, "E2": 2, "E3": 3, "E4": 4, "E5": 5, "E6": 6}
TRI = ("nc", "non", "oui")


# --------------------------------------------------------------------------------------------------------------- grille A

def _ligne(etat):
    if etat == "nc":
        return {"non_calculable": "essai"}
    ok = etat == "oui"
    return {"au_dessus": ok, "passe": ok, "aire": 0.8, "Q": 0.6, "difference": 0.1, "bas": 0.01 if ok else -0.01, "haut": 0.2}


def grille_a(famille: str) -> dict:
    axes = [TRI, TRI, (False, True), TRI, TRI, TRI] + ([TRI, TRI] if famille == "(ii)" else [])
    compte, lignes = 0, Counter()
    for combo in itertools.product(*axes):
        D, Rr, triv, mc, lex, enc = combo[:6]
        te, dd = (combo[6], combo[7]) if famille == "(ii)" else (None, None)
        calc = D != "nc" and Rr != "nc"
        base = calc and D == "oui" and Rr == "oui" and not triv
        lect = all(x == "oui" for x in (mc, lex, enc))
        preds = {"E0": not calc, "E1": calc and D == "non", "E1b": calc and D == "oui" and Rr == "non",
                 "E2": calc and D == "oui" and Rr == "oui" and triv, "E3": base and not lect}
        if famille == "(ii)":
            preds.update({"E4": base and lect and te != "oui", "E5": base and lect and te == "oui" and dd != "oui",
                          "E6": base and lect and te == "oui" and dd == "oui"})
        else:
            preds["E6′"] = base and lect
        vraies = [k for k, v in preds.items() if v]
        if len(vraies) != 1:
            raise SystemExit(f"grille A {famille} : {combo} → {vraies} (trou ou chevauchement)")
        r = {"famille": famille, "D": _ligne(D), "R": _ligne(Rr), "MC": _ligne(mc), "LEX": _ligne(lex), "ENC": _ligne(enc),
             "triviaux": {"t": {"separation": 0.9 if triv else 0.5}}}
        if famille == "(ii)":
            r["TE"], r["DD"] = _ligne(te), _ligne(dd)
        e = lv.etat_cellule(r)["etat"]
        if e != vraies[0]:
            raise SystemExit(f"grille A {famille} : {combo} : prédicats {vraies[0]}, code {e}")
        compte += 1
        lignes[vraies[0]] += 1
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
            raise SystemExit(f"grille B : {v} → {pi}, {pt} (trou ou chevauchement)")
        e = dict(zip(DOSES, v))
        if lv.issue_code(e)[0] != pi[0] or lv.suffixe_code(e)[0] != pt[0]:
            raise SystemExit(f"grille B : désaccord sur {v}")
        ci[pi[0]] += 1
        ct[pt[0]] += 1
    paires = {f"{i} {t}": ci[i] * ct[t] for i in sorted(ci) for t in sorted(ct)}
    total = sum(paires.values())
    if total != 8 ** 8 or len(paires) != 28:
        raise SystemExit(f"grille B : {total} paires, {len(paires)} classes")
    lib = Counter()
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
            lib[(dure, lettre)] += 1
    return {"vecteurs_plafond": 8 ** 4, "vecteurs_transfert": 8 ** 4, "paires": total, "classes_I_suffixe": len(paires),
            "par_paire": paires, "par_issue": dict(ci), "par_suffixe": dict(ct),
            "libelles": {"combinaisons": sum(lib.values()), "dure_et_lettre": lib[(True, True)],
                         "lettre_seule": lib[(False, True)], "aucun": lib[(False, False)],
                         "dure_sans_lettre": lib[(True, False)]}}


def _cellule(etat):
    return {"etat": {"etat": etat, "nom": "jetons_notes", "lecteur": "MC", "lecteurs": ["MC"], "motifs": {}},
            "D": {"aire": 0.62, "bas_echelle_aire": 0.55, "haut_echelle_aire": 0.7, "Q": 0.6},
            "MC": {"difference": 0.01, "bas": -0.02, "haut": 0.04},
            "TE": {"aire": 0.58, "bas_echelle_aire": 0.5, "haut_echelle_aire": 0.66, "Q": 0.6},
            "ART": {"aire": 0.53, "deplacement": False}, "DD": {"difference": 0.05, "bas": 0.01, "haut": 0.09}}


def phrases_28() -> list:
    """Une phrase par paire (I, suffixe), sur des cellules d'essai qui atteignent chaque état."""
    sortie = []
    exemples_i = {"I0": "E0", "I1": "E1", "I2": "E2", "I3": "E3", "I4": "E4", "I5": "E5", "I6": "E6"}
    exemples_t = {"T0": "E0", "T−": "E1", "T±": "E4", "T+": "E6"}
    for i, ei in exemples_i.items():
        for t, et in exemples_t.items():
            pl = {d: _cellule(ei) for d in DOSES}
            tr = {d: _cellule(et) for d in DOSES}
            code, doses = lv.issue_code({d: ei for d in DOSES})
            tc, td = lv.suffixe_code({d: et for d in DOSES})
            if (code, tc) != (i, t):
                raise SystemExit(f"phrases : {i}, {t} non atteintes")
            p = lv.phrase_issue(code, doses, pl) + " " + lv.phrase_suffixe(tc, td, tr) + " " + lv.PHRASE_MODE
            if re.search(r"\{[a-zA-Z_]+\}", p):
                raise SystemExit(f"phrases : crochet non rempli dans {i} {t}")
            sortie.append({"I": i, "T": t, "phrase": p})
    return sortie


# --------------------------------------------------------------------------------------------------------------- grille C

def _pred_p(etats, mus, jugees, variante) -> list:
    tient = (lambda d: etats[d] == "E6" and mus[d] == lv.MU_MUETTE) if variante == cj.RETENUE else \
        (lambda d: etats[d] in ("E5", "E6"))
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
    phrases = {}
    for code in cj.PHRASES_C:
        for famille in ("(ii)", "(i-a)"):
            for variante in (cj.RETENUE, cj.INFORMATION):
                p = cj.phrase_c(code, famille, "motif", "E3 à S50", variante)
                if re.search(r"\{[a-zA-Z_]+\}", p) or "meilleur des deux" in p:
                    raise SystemExit(f"grille C : phrase {code} {famille} {variante} fautive")
                if famille == "(i-a)" and "à texte égal" in p:
                    raise SystemExit(f"grille C : « à texte égal » non omis pour (i-a) ({code})")
                phrases[f"{code} {famille} {variante}"] = p
    return {"combinaisons_ii": n, "par_ligne": {v: dict(c) for v, c in comptes.items()}, "combinaisons_ia": sum(ia.values()),
            "par_ligne_ia": dict(ia), "trous": 0, "chevauchements": 0, "phrases": phrases}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="énumération des grilles de lecture de B bis")
    ap.add_argument("--sortie", default=None)
    a = ap.parse_args(argv)
    r = {"A": {"(ii)": grille_a("(ii)"), "(i-a)": grille_a("(i-a)")}, "B": grille_b(), "C": grille_c(), "phrases_28": phrases_28()}
    texte = json.dumps(r, indent=1, ensure_ascii=False, sort_keys=True, default=str)
    if a.sortie:
        with open(a.sortie, "x", encoding="utf-8") as f:
            f.write(texte + "\n")
    print(f"A (ii) {r['A']['(ii)']['combinaisons']}, A (i-a) {r['A']['(i-a)']['combinaisons']}, B {r['B']['paires']} paires en "
          f"{r['B']['classes_I_suffixe']} classes, libellés {r['B']['libelles']['combinaisons']}, 28 phrases, "
          f"C {r['C']['combinaisons_ii']} + {r['C']['combinaisons_ia']} : 0 trou, 0 chevauchement")
    return 0


if __name__ == "__main__":
    sys.exit(main())
