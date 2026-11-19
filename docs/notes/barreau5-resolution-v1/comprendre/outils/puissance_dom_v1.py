"""Calculs simples de puissance sur les lignes « dommage par action » de l'étape B bis.
N'ouvre que le fichier de lecture de l'étape B bis (champs publiés : effectifs, comptes, Q, bornes) ; aucun score.
Formule A (texte de validité de l'adaptateur, l. 80 et l. 134 ; reprise par le préenregistrement de l'étape B bis, l. 61) :
  sigma(n1, n0) = 1,188 * racine((n1 + n0 + 1) / (12 n1 n0)) ;
  aire minimale détectable à 80 %, ligne lue contre son plancher par la règle (a), niveau z :
  0,5 + (1,645 + 1,10 * (z + 0,842)) * sigma.
Formule B (préenregistrement de l'étape B bis, l. 202 et l. 208, « Lecture d'un nul ») :
  aire minimale = Q + (z + 0,842) * s, s = demi-largeur de l'intervalle de D lue au résultat / z.
"""
import json, math, sys
p = sys.argv[1]
r = json.load(open(p))["resultat"]["cellules"]
Z95, Z99, Z80 = 1.959964, 2.575829, 0.841621

def sigma(n1, n0):
    return 1.188 * math.sqrt((n1 + n0 + 1) / (12.0 * n1 * n0))

def aire_min_A(s, z=Z95):
    return 0.5 + (1.645 + 1.10 * (z + 0.842)) * s

print("== Formule A : par les seuls effectifs (95 %)")
print("cellule ligne | pli e0 (gonflées, non gonflées) sigma aire_min | pli e1 ... | deux plis : sigma de la moyenne, aire_min | comptes réunis : sigma, aire_min")
for nom in ("P-S25", "P-S50", "P-S75", "P-S100"):
    for ligne in ("DOM", "DOM_H"):
        o = r[nom][ligne]
        e = o["effectifs"]
        s = [sigma(x["positifs"], x["negatifs"]) for x in e]
        sm = 0.5 * math.sqrt(s[0] ** 2 + s[1] ** 2)
        c = o["comptes"]
        sp = sigma(c["gonflees"], c["non_gonflees"])
        print(f"{nom} {ligne} | e0 ({e[0]['positifs']}, {e[0]['negatifs']}) {s[0]:.4f} {aire_min_A(s[0]):.3f} | "
              f"e1 ({e[1]['positifs']}, {e[1]['negatifs']}) {s[1]:.4f} {aire_min_A(s[1]):.3f} | "
              f"moyenne {sm:.4f} {aire_min_A(sm):.3f} | réunis ({c['gonflees']}, {c['non_gonflees']}) {sp:.4f} {aire_min_A(sp):.3f}"
              f" | non informative (sigma > 0,060) : plis {[x > 0.060 for x in s]}, réunis {sp > 0.060}")
c = r["P-instruit"]["DOM"]["comptes"]
sp = sigma(c["gonflees"], c["non_gonflees"])
print(f"P-instruit DOM | réunis ({c['gonflees']}, {c['non_gonflees']}) sigma {sp:.4f} aire_min {aire_min_A(sp):.3f} ; {r['P-instruit']['DOM'].get('non_calculable')}")
print("contrôle de la formule : (100, 300) à 95 % ->", round(aire_min_A(sigma(100, 300)), 4), "(le texte écrit ≈ 0,687) ; à 97,5 % ->",
      round(aire_min_A(sigma(100, 300), 2.241403), 4), "(le texte de validité écrit 0,700) ; sigma(640, 640) =", round(sigma(640, 640), 6), "(le texte écrit 0,019179)")

print()
print("== Formule B : par le Q et la demi-largeur lus au résultat (95 %)")
print("cellule ligne | aire | Q | D [bas ; haut] | demi-largeur | s | aire minimale détectable à 80 % | intervalle propre de l'aire")
for nom in ("P-S25", "P-S50", "P-S75", "P-S100"):
    for ligne in ("DOM",):
        o = r[nom][ligne]
        w = (o["haut"] - o["bas"]) / 2.0
        s = w / Z95
        print(f"{nom} {ligne} | {o['aire']:.4f} | {o['Q']:.4f} | {o['D']:+.4f} [{o['bas']:+.4f} ; {o['haut']:+.4f}] | {w:.4f} | {s:.4f} | "
              f"{o['Q'] + (Z95 + Z80) * s:.3f} | [{o['bas_sonde']:.4f} ; {o['haut_sonde']:.4f}]")

print()
print("== Plafond de la différence « texte égal moins artefact » (99 %)")
print("cellule | TE | ART | 1 - ART (différence la plus grande possible) | DD [bas ; haut] | demi-largeur | s | différence minimale détectable à 80 % | atteignable ?")
for nom in ("P-S25", "P-S50", "P-S75", "P-S100", "T-instruit-S25", "T-instruit-S50", "T-instruit-S75", "T-instruit-S100"):
    o = r[nom]
    dd = o["DD"]
    w = (dd["haut"] - dd["bas"]) / 2.0
    s = w / Z99
    dmin = (Z99 + Z80) * s
    marge = 1.0 - o["ART"]["aire"]
    print(f"{nom} | {o['TE']['aire']:.4f} | {o['ART']['aire']:.4f} | {marge:.4f} | {dd['difference']:+.4f} [{dd['bas']:+.4f} ; {dd['haut']:+.4f}] | "
          f"{w:.4f} | {s:.4f} | {dmin:.4f} | {'oui' if marge >= dmin else 'non'} (TE requis >= {o['ART']['aire'] + dmin:.4f})")
