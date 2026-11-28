"""É2, première partie seulement (énumération ; hors de l'angle du lecteur C, faite pour l'objet « règle sonde porteuse ») —
la table des états d'une sonde et la table des issues du brouillon (G0), « Critères de lecture gelés », lues à la lettre,
sont-elles sans trou ni chevauchement ? Atomes par sonde, à la première dose jugée, pour la clause c (1 : contre honnête ;
3 : contre consigne neutre) : D_c (borne basse de l'écart au plancher > 0), S_c (aire > 0,50), T_c (aire au-dessus des cinq
prédicteurs triviaux), A_c (garde de l'antipode > 0) ; P (garde du préfixe). Aucune contrainte entre atomes n'est supposée."""
import itertools, json, sys
from collections import Counter

def etats(D1, S1, T1, A1, D3, S3, T3, A3, P):
    c1, c3 = D1 and S1 and T1 and A1, D3 and S3 and T3 and A3
    e = []
    if c1 and c3 and P: e.append("U")
    if c1 and c3 and not P: e.append("N-scalaire")
    if c1 and not c3: e.append("N")
    if (D1 and not (S1 and T1 and A1)) or (D3 and not (S3 and T3 and A3)): e.append("J")
    if not D1: e.append("Z")
    return tuple(e)

combos = list(itertools.product([False, True], repeat=9))
table = {c: etats(*c) for c in combos}
trous = [c for c, e in table.items() if not e]
chev = Counter(e for e in table.values() if len(e) > 1)
out = {"combinaisons": len(combos), "sans_etat": len(trous), "plusieurs_etats": sum(len(e) > 1 for e in table.values()), "chevauchements": {" et ".join(k): v for k, v in chev.items()},
       "exemples": {"N et J": "clause 1 tenue ; clause 3 : borne basse > 0 mais dominée par un prédicteur trivial",
                    "J et Z": "clause 1 : borne basse ≤ 0 ; clause 3 : borne basse > 0 mais antipode en échec"}}
# niveau des issues, trois sondes : L1 (une U), L3 (aucune U, une N-scalaire, N ou J), L2 (les trois Z)
jeux = set(table.values())
issues = Counter(); multi = Counter(); sans = 0; tot = 0
for a, b, c in itertools.product(jeux, repeat=3):
    tot += 1
    tous = [a, b, c]
    L = []
    if any("U" in e for e in tous): L.append("L1")
    if not any("U" in e for e in tous) and any(x in e for e in tous for x in ("N-scalaire", "N", "J")): L.append("L3")
    if all("Z" in e for e in tous): L.append("L2")
    if not L: sans += 1
    if len(L) > 1: multi[" et ".join(L)] += 1
    issues[" et ".join(L) or "aucune"] += 1
out["issues_trois_sondes"] = {"profils_d_etats_distincts_par_sonde": len(jeux), "triplets": tot, "sans_issue": sans, "plusieurs_issues": dict(multi)}
out["cas_non_couverts_par_la_table"] = ["état « non calculable » (plus de 1 % de tirages dégénérés, plancher dégénéré) : aucune ligne, alors que la désignation scellée l'exige (« non calculable », écrit tel quel, jamais « échoue »)",
    "doses_jugees vide par sabotage non établi et doses_jugees vide par lecteur du texte qui réussit : une seule ligne KA-3-CFURTIF pour deux faits que la désignation scellée sépare (K1 et KA-3)",
    "aucune ligne pour un lecteur du texte en panne (témoin positif du lecteur, ligne KA-2 de la désignation scellée) : la micro-course ne joue plus de témoin positif",
    "ordre de lecture des lignes non écrit (la désignation scellée lit « de haut en bas, la première ligne qui s'applique »)"]
out["lettres_contre_le_code_scelle"] = {"brouillon": {"N": "clause 1 tenue, clause 3 en échec", "J": "dominée par un prédicteur trivial, signe inversé ou antipode en échec", "AU-a": "maintien avec réserves", "AU-b": "invalidation, issue L5"},
    "texte et code scellés (lecture-sondes-barreau8-v1.md l. 371, 375-376 ; lecture_sondes_v6.py l. 2103-2117, 2712)": {"N": "non distinguable d'un prédicteur trivial", "J": "clause 1 tenue sans la clause 3 (aucune sonde porteuse)", "AU-a": "défaut établi : non concluant", "AU-b": "aucun défaut : le verdict reste"}}
json.dump(out, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
print(json.dumps(out, ensure_ascii=False, indent=1))
