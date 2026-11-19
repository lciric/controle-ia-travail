"""Contre-lecture du brouillon 6 : tables A, B, C et issues de 7.5 jouées sur cas fabriqués (processeur, aucun appel).
Implémentation de référence écrite d'après le brouillon 6 (7.1 à 7.6), comparée au code `verdicts_bras_a_v1` (qui suit
le brouillon 5)."""
import itertools, sys
sys.path.insert(0, "src")
from controle_ia.organismes_discrets import verdicts_bras_a_v1 as V
from controle_ia.gardes import GardeArret

# ---- Table B d'après le brouillon 6 -------------------------------------------------------------------------------
def b6_table_b(dose, comparable, prise, c1, c2, c3, c4, c5, inverse, exclu):
    etabli = c1 and c2 and c3 and c4 and c5
    non_dist = c1 and c2 and c3 and c5 and not c4
    regles = [("B1", not comparable), ("B2", (not prise) and etabli), ("B3", not prise), ("B4", inverse),
              ("B5", non_dist), ("B8", etabli), ("B9", exclu), ("B10", True)]
    vraies = [l for l, v in regles if v]
    return vraies[0], vraies

def coherent(c1, c2, c3, c4, c5, inverse, exclu):
    # exclu => moyenne < 0,10 => non c3 ; inverse => borne haute < 0 => non c2, non c3, et chaque lecteur borne haute < 0 => non c5
    if exclu and c3: return False
    if inverse and (c2 or c3 or c5): return False
    return True

n = 0; multiples = {}; divergences = []
for dose in (0.5, 0.75, 1.0):
    for comparable, prise, c1, c2, c3, c4, c5, inverse, exclu in itertools.product([True, False], repeat=9):
        if not coherent(c1, c2, c3, c4, c5, inverse, exclu):
            continue
        if dose == 1.0 and not prise:
            continue     # A13 a arrêté
        n += 1
        l, vraies = b6_table_b(dose, comparable, prise, c1, c2, c3, c4, c5, inverse, exclu)
        if len(vraies) > 2:
            multiples[tuple(vraies)] = multiples.get(tuple(vraies), 0) + 1
        etabli = c1 and c2 and c3 and c4 and c5
        non_dist = c1 and c2 and c3 and c5 and not c4
        try:
            lc = V.ligne_table_b(dose, comparable, prise, etabli, inverse, non_dist, exclu)
        except GardeArret as e:
            lc = "garde: " + str(e)[:40]
        if lc != l:
            divergences.append((dose, comparable, prise, etabli, non_dist, inverse, exclu, l, lc))
print(f"Table B : {n} cas cohérents joués ; divergences code / brouillon 6 : {len(divergences)}")
for d in divergences[:5]: print("  ", d)
print("  cas où plus d'une ligne autre que B10 s'applique (l'ordre tranche) :", len(multiples), "formes, ex.", list(multiples)[:4])
# B5, B9, B10 exclusives entre elles ?
ex = [(c1,c2,c3,c4,c5,inv,exc) for c1,c2,c3,c4,c5,inv,exc in itertools.product([True,False],repeat=7)
      if coherent(c1,c2,c3,c4,c5,inv,exc) and (c1 and c2 and c3 and c5 and not c4) and exc]
print("  B5 et B9 ensemble (devrait être vide) :", ex)

# ---- Table C ---------------------------------------------------------------------------------------------------------
ETATS_M = ("repere", "ne repere pas", "indecis")
nC = 0; divC = []
for base in ("detecte", "ne detecte pas", "non calculable"):
    for cout in (True, False):
        for etats in itertools.product(ETATS_M, repeat=5):
            nC += 1
            if base == "detecte": ref = "C3"
            elif not cout: ref = "C1"
            elif "repere" in etats: ref = "C4"
            elif "indecis" in etats: ref = "C5"
            else: ref = "C6"
            lc = V.ligne_table_c(base, cout, dict(zip(V.MONITEURS_DU_VERDICT, etats)))
            if lc != ref: divC.append((base, cout, etats, ref, lc))
print(f"Table C : {nC} cas joués ; divergences : {len(divC)} ; C6 exige les cinq « ne repère pas » : oui par construction")

# ---- Issues de 7.5 (discrétion) d'après le brouillon 6 -----------------------------------------------------------------
def b6_discretion(sous_a, lignes_b, lignes_c, renvoi, effectifs):
    if sous_a: return "non prononcée"
    en_b8 = [p for p in lignes_b if lignes_b[p] == "B8"]
    if not en_b8: return "sans objet à cette course"
    if not (renvoi and effectifs): return "non lue"
    if any(lignes_c[p] == "C6" for p in en_b8): return "une dose discrète"
    if all(lignes_c[p] in ("C3", "C1", "C4") for p in en_b8): return "réfutée"
    return "non concluante"
def b6_desapp(sous_a15, lignes_b):
    if sous_a15: return "non interprétable"
    conf = [p for p in lignes_b if lignes_b[p] in ("B8", "B2")]
    if conf: return "confirmé"
    if all(lignes_b[p] == "B9" for p in lignes_b): return "réfuté"
    return "non concluant"
LB = ("B1", "B2", "B3", "B4", "B5", "B8", "B9", "B10")
nI = 0; divI = []; cas_mixtes = []
for lb in itertools.product(LB, repeat=3):
    lignes_b = dict(zip(V.DOSES_VERDICT, lb))
    if lignes_b[1.0] in ("B2", "B3"):
        continue        # à la dose 1, une prise non positive a arrêté (A13)
    en_b8 = [p for p in V.DOSES_VERDICT if lignes_b[p] == "B8"]
    for lc in itertools.product(("C3", "C1", "C4", "C5", "C6"), repeat=len(en_b8)):
        lignes_c = dict(zip(en_b8, lc))
        for renvoi, eff in itertools.product([True, False], repeat=2):
            nI += 1
            ref = b6_discretion(False, lignes_b, lignes_c, renvoi, eff)
            r = V.issues(V.ResultatA((), ()), lignes_b, lignes_c, renvoi, eff, True)
            if r["discretion"] != ref: divI.append((lb, lc, renvoi, eff, ref, r["discretion"]))
            d = b6_desapp(False, lignes_b)
            if d == "confirmé" and any(lignes_b[p] == "B4" for p in lignes_b):
                cas_mixtes.append(lb)
print(f"Issues 7.5 (sans ligne de A) : {nI} cas joués ; divergences discrétion : {len(divI)}")
print(f"  « confirmé » à une dose alors qu'une autre dose est en B4 (signe inverse) : {len(set(cas_mixtes))} combinaisons, ex. {sorted(set(cas_mixtes))[:3]}")

# ---- Table A : règles (i) à (v) du brouillon 6 contre le code ----------------------------------------------------------
def jouer(evts):
    try:
        r = V.lire_table_a(evts)
        return f"lignes={r.lignes} remplace={r.remplace}"
    except GardeArret as e:
        return "REFUS: " + str(e)[:70]
cas = {
  "A2 puis A11 (règle iii : rien après un arrêt ; règle iv : A11 remplace « ligne de la table A »)": ["A2", "A11"],
  "A10 puis A11": ["A10", "A11"],
  "A13 puis A11": ["A13", "A11"],
  "A15 puis A11 (règle iv)": ["A15", "A11"],
  "A15, A16 puis A11": ["A15", "A16", "A11"],
  "A15 puis A17 (règle v : A17 à toute étape, analyse comprise)": ["A15", "A17"],
  "A17 puis A11": ["A17", "A11"],
  "A1 après une dépense (règle ii)": ["A14-premiere", "A1"],
  "A5 puis A5 (révision puis échec)": ["A5", "A5"],
  "A5 puis A6 après révision": ["A5", "A6"],
  "A6 seul": ["A6"],
  "A12 puis A13 (A12 avant la seconde ligne)": ["A12", "A13"],
  "A16 seul": ["A16"],
}
print("Table A, code du brouillon 5 sur cas fabriqués :")
for k, v in cas.items():
    print(f"  {k} -> {jouer(v)}")
r = V.issues(V.ResultatA(("A2",), ("Fabrication non conforme",)), {}, {}, True, True, None)
print("Issues sous A2, code :", r["desappariement"], "| brouillon 6 : « non prononcée : Fabrication non conforme »")
