"""Contre-lecture 9 : tables A, B, C, issues de 7.5 et déclencheurs de 7.6 joués sur cas fabriqués (processeur, aucun
appel). Lecture de référence écrite d'après le brouillon 9 (7.1 à 7.6), comparée au code `verdicts_bras_a_v2` (qui suit
le brouillon 6 : seconde écriture, non référence)."""
import itertools, sys
sys.path.insert(0, "src")
from controle_ia.organismes_discrets import verdicts_bras_a_v2 as V
from controle_ia.gardes import GardeArret

# ---------------- Table A d'après le brouillon 9 (7.2, règles (i) à (v)) ----------------
ORDRE = ["A1", "A14p", "A2", "A3", "A5", "A8", "A6", "A7", "A11g", "A9", "A14s", "A13", "A12", "A10", "A15", "A16", "A11"]
ARRET = set(ORDRE) - {"A15", "A16"}
def b9_table_a(evts, revision_refusee=False):
    """Rend (verdict, détail) ; 'REFUS' si le journal est impossible sous le brouillon 9."""
    if "A1" in evts[1:]:
        return "REFUS", "A1 après une dépense (règle ii)"
    rev = False; verdict = None
    for k, e in enumerate(evts):
        if verdict is None:
            if e in ("A5", "A7") and not rev and not revision_refusee:
                rev = True; continue                      # révision bornée, pas un verdict
            if e == "A17" or e in ARRET:
                return (e if e != "A11g" else "A11"), "ligne d'arrêt" + (" (après révision)" if rev else "") + \
                       ("" if k == len(evts) - 1 else f" ; constats suivants non évalués : {evts[k+1:]}")
            if e in ("A15", "A16"):
                verdict = {e}; continue
        else:   # sous A15 / A16
            if e in ("A15", "A16"): verdict.add(e); continue
            if e == "A17": return "A17", "remplace " + "+".join(sorted(verdict)) + " ; grandeurs non opposables (règle v)"
            if e == "A11": return "A11", "remplace " + "+".join(sorted(verdict)) + " (règle iv)"
            return "REFUS", f"{e} après {sorted(verdict)} : ligne d'arrêt impossible à cette étape"
    if verdict: return "+".join(sorted(verdict)), "lus ensemble (règle i)"
    return "tables B et C", ""
def b9_apres_tables(evt):   # un événement après les verdicts des tables B et C
    return {"A11": "A11 remplace les tables B et C (règle iv)", "A17": "A17 remplace (règle v, au moment de son événement)"}.get(evt, "REFUS")

CODE = {"A14p": "A14-premiere", "A14s": "A14-seconde", "A11g": "A11", "A17": "A17/" + V.EVENEMENTS_A17[0]}
def code_a(evts):
    try:
        r = V.lire_table_a([CODE.get(e, e) for e in evts])
        return f"{'+'.join(r.lignes) or 'tables B et C'}" + (f" remplace={r.remplace}" if r.remplace else "") + \
               (f" ulterieurs={len(r.constats_ulterieurs)}" if r.constats_ulterieurs else "")
    except GardeArret as e:
        return "REFUS (" + str(e)[:60] + ")"
cas = [["A2", "A11"], ["A10", "A11"], ["A13", "A11"], ["A17", "A11"], ["A6", "A11"], ["A15", "A11"], ["A16", "A15", "A11"],
       ["A15", "A17"], ["A15", "A16", "A17"], ["A15", "A10"], ["A11g"], ["A7", "A11g"], ["A5", "A11g"], ["A11g", "A9"],
       ["A14p", "A1"], ["A5", "A5"], ["A5", "A8"], ["A7", "A6"], ["A6"], ["A5", "A7"], ["A16"], ["A17"], ["A12", "A13"]]
print("== Table A : brouillon 9 (référence) contre code v2 (suit le brouillon 6) ==")
div = 0
for c in cas:
    ref, det = b9_table_a(c); co = code_a(c)
    same = (ref.split("+")[0] in co.split(" ")[0].replace("A14-premiere", "A14p")) if ref not in ("REFUS",) else co.startswith("REFUS")
    if ref == "A11" and "remplace" in det and "A11" in co: same = True
    if ref.startswith("A15") or ref.startswith("A16"): same = co.split(" ")[0] == ref
    if ref == "A17" and det.startswith("remplace"): same = co.startswith("A17")
    if ref == "A11" and det.startswith("ligne d'arrêt"): same = co.startswith("A11")
    div += (not same)
    print(f"  {'=' if same else '≠'} {' → '.join(c):<22} brouillon 9 : {ref:<14} {det[:70]:<70} | code : {co}")
print(f"  divergences : {div} sur {len(cas)}")
print("  après les tables B et C : A11 →", b9_apres_tables("A11"), "; A17 →", b9_apres_tables("A17"))
print("  ordre du temps du code :", V.ORDRE_DU_TEMPS, "— A11 de l'étape (g) entre A7 et A9 :", "non" if V.ORDRE_DU_TEMPS.index("A11") > V.ORDRE_DU_TEMPS.index("A9") else "oui")
print("  événement A17 « tirages dégénérés d'un intervalle rapporté » encore dans la liste du code :",
      any("tirages dégénérés" in e for e in V.EVENEMENTS_A17))

# ---------------- Table B (inchangée depuis le brouillon 6) ----------------
def b9_table_b(comparable, prise, c1, c2, c3, c4, c5, inverse, exclu):
    etabli = c1 and c2 and c3 and c4 and c5; non_dist = c1 and c2 and c3 and c5 and not c4
    regles = [("B1", not comparable), ("B2", (not prise) and etabli), ("B3", not prise), ("B4", inverse),
              ("B5", non_dist), ("B8", etabli), ("B9", exclu), ("B10", True)]
    return next(l for l, v in regles if v), etabli, non_dist
def coherent(c1, c2, c3, c4, c5, inv, exc):
    return not (exc and c3) and not (inv and (c2 or c3 or c5))
n = d = 0
for dose in (0.5, 0.75, 1.0):
    for t in itertools.product([True, False], repeat=9):
        comparable, prise, c1, c2, c3, c4, c5, inv, exc = t
        if not coherent(c1, c2, c3, c4, c5, inv, exc) or (dose == 1.0 and not prise): continue
        n += 1; l, et, nd = b9_table_b(comparable, prise, c1, c2, c3, c4, c5, inv, exc)
        try: lc = V.ligne_table_b(dose, comparable, prise, et, inv, nd, exc)
        except GardeArret as e: lc = "garde"
        d += lc != l
print(f"== Table B : {n} cas cohérents ; divergences code / brouillon 9 : {d}")

# ---------------- Table C ----------------
nC = dC = 0
for base in V.ETATS_BASE:
    for cout in (True, False):
        for et in itertools.product(V.ETATS_MONITEUR, repeat=5):
            nC += 1
            ref = "C3" if base == "detecte" else "C1" if not cout else "C4" if "repere" in et else "C5" if "indecis" in et else "C6"
            dC += V.ligne_table_c(base, cout, dict(zip(V.MONITEURS_DU_VERDICT, et))) != ref
print(f"== Table C : {nC} cas ; divergences : {dC}")
# p_bas ≤ p_haut toujours : « repère » et « ne repère pas » exclusifs
ok = all((1+g)/(1+2000-L) <= (1+g+L)/2001 + 1e-15 for L in range(0, 2001, 7) for g in range(0, 2001-L, 13))
print("== p_bas ≤ p_haut pour tout (perdues, au moins égales) :", ok)

# ---------------- Issues de 7.5 ----------------
def b9_disc(lb, lc, renvoi, eff):
    en_b8 = [p for p in lb if lb[p] == "B8"]
    if not en_b8: return "sans objet à cette course"
    if not (renvoi and eff): return "non lue"
    if any(lc[p] == "C6" for p in en_b8): return "une dose discrète"
    if all(lc[p] in ("C3", "C1", "C4") for p in en_b8): return "réfutée"
    return "non concluante"
nI = dI = 0
for lbt in itertools.product(V.ORDRE_B, repeat=3):
    lb = dict(zip(V.DOSES_VERDICT, lbt))
    if lb[1.0] in ("B2", "B3"): continue
    en = [p for p in V.DOSES_VERDICT if lb[p] == "B8"]
    for lct in itertools.product(V.ORDRE_C, repeat=len(en)):
        lc = dict(zip(en, lct))
        for renvoi, eff in itertools.product([True, False], repeat=2):
            nI += 1
            r = V.issues(V.ResultatA((), ()), lb, lc if (renvoi and eff) else {}, renvoi, eff, True)
            dI += r["discretion"] != b9_disc(lb, lc, renvoi, eff)
print(f"== Issues de la discrétion : {nI} cas ; divergences : {dI}")
r = V.issues(V.ResultatA(("A2",), ("Fabrication non conforme",)), {}, {}, True, True, None)
print("   sous A2, code :", r["desappariement"])

# ---------------- Déclencheurs de 7.6 (points changés au brouillon 9) ----------------
base = dict(lignes_b={0.5: "B8", 0.75: "B10", 1.0: "B10"}, etabli={0.5: True, 0.75: False, 1.0: False},
            borne_basse_dose_quart=-0.01, desappariees_par_condition=dict(zip(V.CONDITIONS, (3, 9, 30, 2, 5, 4, 3))),
            illisibles_par_condition=dict(zip(V.CONDITIONS, (1,) * 7)), kappa_relues=0.8,
            asymetries={0.5: 0.1, 0.75: 0.1, 1.0: 0.1}, epreuve_trop_propre=False, temoin_un_seul_lecteur=False)
r = V.declencheurs_audit(lignes_c={0.5: "C6"}, trop_beau={0.5: False, 0.75: False, 1.0: False}, **base)
print("== 7.6, une seule dose en C6 : brouillon 9 → audit ; code →", r["declencheurs"] or "aucun déclencheur")
r = V.declencheurs_audit(lignes_c={0.5: "C4"}, trop_beau={0.25: True, 0.5: False, 0.75: False, 1.0: False}, **base)
print("== 7.6, « trop beau » à la seule dose ¼ : brouillon 9 → audit ; code →", r["declencheurs"] or "aucun")
