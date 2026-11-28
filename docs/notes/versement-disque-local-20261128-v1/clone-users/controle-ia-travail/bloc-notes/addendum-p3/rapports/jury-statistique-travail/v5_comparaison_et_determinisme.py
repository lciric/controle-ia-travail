"""Même source, même lecture, mêmes graines : A et B ; déterminisme octet pour octet ; entrées intactes."""
import copy, json, time
import numpy as np
from commun import A, B
from donnees import completer, lecture, G, reduire, P, _source

reduire()
src = completer(_source(0)); lec = lecture(src)
def canon(x): return json.dumps(x, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
def egal(x, y):
    if isinstance(x, dict):
        return set(x) == set(y) and all(egal(x[k], y[k]) for k in x)
    if isinstance(x, list):
        return len(x) == len(y) and all(egal(a, b) for a, b in zip(x, y))
    if isinstance(x, np.ndarray):
        return np.array_equal(x, y, equal_nan=x.dtype.kind == "f")
    return x == y
for nom, M in (("A", A), ("B", B)):
    s0, l0, g0 = copy.deepcopy(src), copy.deepcopy(lec), copy.deepcopy(G)
    t = time.time(); r1 = M.analyser_addendum(src, lec, G); t1 = time.time() - t
    r2 = M.analyser_addendum(src, lec, G)
    print(f"{nom} : {t1:.1f} s ; deux passages identiques octet pour octet : {canon(r1) == canon(r2)} ; "
          f"entrées intactes : source {egal(s0, src)}, lecture {egal(l0, lec)}, graines {egal(g0, G)}")
    if nom == "A": ra = r1
    else: rb = r1
print("réserves A :", [r["reserve"] for r in ra["reserves_addendum"]], "| réserves B :",
      [r["nom"] for r in rb["synthese"]["reserves_addendum"]])
print("issue lecture :", lec["issue"]["ligne"])
# A1 : estimations ponctuelles égales ; intervalles (générateurs différents) voisins
for p in P:
    for jeu in ["saboteur-honnete", "saboteur-temoin", "temoin-honnete", "mention-honnete", "saboteur-mention", "T1", "T4"]:
        a = ra["analyses"]["A1"][p]["descriptif"]["controles"][jeu]; b = rb["analyses"]["A1"][p]["descriptif"][jeu]
        print(f"A1 {p[:9]} {jeu:17s} aire A {a['aire']:.6f} B {b['aire']:.6f} | Q A {a['plancher_quantile']:.6f} "
              f"B {b['plancher_quantile']:.6f} | Δ_bas A {a['ecart_bas']:+.4f} B {b['ecart_bas']:+.4f} | niveau {a['niveau']} {b['niveau']}")
for p in P:
    a = ra["analyses"]["A2"][p]["descriptif"]["controles"]; b = rb["analyses"]["A2"][p]["descriptif"]
    print(f"A2 {p[:9]} aire coût A {a['aire_cout']['aire']:.6f} [{a['aire_cout']['bas']:.6f}] B {b['a_aire_cout']['aire']:.6f} "
          f"[{b['a_aire_cout']['bas']:.6f}] | fenêtres moyenne obs A {a['difference_fenetre_meme_longueur']['difference_observee_moyenne_des_repliques']:.6f} "
          f"B {b['b_fenetre_meme_longueur']['difference_moyenne_des_repliques']:.6f} bas A {a['difference_fenetre_meme_longueur']['bas']:+.4f} B {b['b_fenetre_meme_longueur']['bas']:+.4f}")
    a5 = ra["analyses"]["A5"][p]["descriptif"]["controles"]["T2_propre"]; b5 = rb["analyses"]["A5"][p]["descriptif"]["T2_propre"]
    print(f"A5 {p[:9]} T2_propre A diff {a5['difference']:.6f} bas {a5['bas']:.6f} n {a5['n_actions']} | B diff {b5['difference']:.6f} bas {b5['bas']:.6f}")
    a4 = ra["analyses"]["A4"][p]["descriptif"]["controles"]; b4 = rb["analyses"]["A4"][p]["descriptif"]
    print(f"A4 {p[:9]} (a) aire A {a4['T4_tranches_internes']['aire']:.6f} B {b4['a_T4_tranches_internes']['aire']:.6f} "
          f"(b) aire A {a4['T1_intra_tache']['aire']:.6f} B {b4['b_T1_intra_tache']['aire']:.6f} "
          f"Q A {a4['T1_intra_tache']['plancher_quantile']:.6f} B {b4['b_T1_intra_tache']['plancher_quantile']:.6f} "
          f"(c) aire A {a4['T1_reference_log_moyenne']['aire']:.6f} B {b4['c_T1_sensibilite']['aire']:.6f}")
    a3 = ra["analyses"]["A3"][p]["descriptif"]["controles"]; b3 = rb["analyses"]["A3"][p]["descriptif"]["contrastes"]
    print(f"A3 {p[:9]} Δ_ST A {a3['saboteur_moins_temoin']['difference']:.6f} B {b3['ST']['difference']:.6f} ; Δ_SM A "
          f"{a3['saboteur_moins_mention']['difference']:.6f} B {b3['SM']['difference']:.6f}")
a6 = ra["analyses"]["A6"]["descriptif"]["controles"]; b6 = rb["analyses"]["A6"]["toutes"]["descriptif"]
print(f"A6 P3-P1 effet A {a6['P3-P1_etendu']['effet']:.6f} B {b6['P3-P1']['effet']:.6f} ; lecture {lec['P3-P1']['effet']:.6f}")
