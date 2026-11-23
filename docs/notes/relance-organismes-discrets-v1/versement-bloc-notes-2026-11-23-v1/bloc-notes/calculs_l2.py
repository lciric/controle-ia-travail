# Calculs du complément de devis de la ligne 2 (bras A). Entrées : manifeste de la ligne 1 (clé resume), devis v5 (5.1, 5.2, 3.3).
import math
h = lambda s: s / 3600
# Mesures de la ligne 1 (manifeste-de-la-ligne-1.json, clé resume)
duree, eps, act, coup = 4596.4681555219995, 128, 1280, 104
gen_s, passes, jgen = 4542.726181091997, 53912, 292813
pu_s, pu_j = 50.73237615299513, 538098
mer_s = 243.31626677513123
cumul, fixes, taux = 2.6325220931095106, 1.0416666666666667, 1.1833333333333333
d = duree / eps
print(f"d = {d:.4f} s/ép ; génération {gen_s/eps:.4f} s/ép ; part génération {gen_s/duree:.4f}")
print(f"écart à 40,2 : {d/40.2-1:+.4f} ; à 42,8 : {d/42.8-1:+.4f}")
print(f"jetons générés/action {jgen/act:.2f} (vs 223 : {jgen/act/223-1:+.4f}) ; par épisode {jgen/eps:.1f}")
print(f"passe par décodage {1000*gen_s/passes:.2f} ms ; passes par pas de lot {passes/160:.2f} ; borne 400 : x{400/(passes/160):.4f}")
dmax = (gen_s/16*400/(passes/160) + (duree-gen_s)/16)/8   # chaque pas de chaque lot à 400 passes, même coût par passe
print(f"épisode si chaque pas de lot va à 400 passes : {dmax:.2f} s")
print(f"passe unique {pu_s/eps:.4f} s par transcription de {pu_j/eps:.1f} jetons")
print(f"mise en route {mer_s:.1f} s = {h(mer_s):.4f} h ; coupées {coup/act:.5f}")
print(f"compteur : durée comptée {(cumul-fixes)/taux:.4f} h ; frais fixes = 40 Go x {fixes/40:.6f}")
# Ligne 2 : postes (devis v5, 5.1), bas sur mesure, haut sur les hypothèses hautes du devis v5
ident = 6 * 3 / 60
Hb = h(mer_s) + h(2304*2.1) + ident + h(896*d) + h(1280*pu_s/eps)
Hh = 1.0 + h(2304*3.0) + ident + h(896*42.8) + h(1280*0.45)
print(f"L2 heures : bas {Hb:.4f} (mer {h(mer_s):.4f}, dist {h(2304*2.1):.4f}, ident {ident:.2f}, rejeu {h(896*d):.4f}, prise {h(1280*pu_s/eps):.4f})")
print(f"            haut {Hh:.4f} (dist {h(2304*3.0):.4f}, rejeu {h(896*42.8):.4f}, prise {h(1280*0.45):.4f})")
Ab = Hb * 1.1833333333333333 + fixes
Ah = Hh * 1.30 + 2.0
print(f"attendu : {Ab:.4f} à {Ah:.4f} USD")
# Plafond recalculé (devis v5, 5.2)
k = ident + h(2304*6.0) + h(1280*0.90)
H2 = lambda dd, m=1.0: max(1.0, m) + k + 896*dd/3600
P2 = lambda dd, m=1.0: 2*1.38*H2(dd, m) + 4
for dd, m in ((d, h(mer_s)), (d, 0.0), (40.0, 1.0), (42.8, 1.0), (45.0, 1.0)):
    print(f"  d={dd:.2f}, m={m:.4f} : H2={H2(dd,m):.4f} h ; P2={P2(dd,m):.4f} -> {math.ceil(P2(dd,m))}")
print(f"  sans le max : {2*1.38*(h(mer_s)+k+896*d/3600)+4:.4f}")
# Règle du pire cas de 3.3 (x4) sur les heures hautes recalculées, débit mesuré
Hhm = 1.0 + h(2304*3.0) + ident + h(896*d) + h(1280*0.45)
print(f"x4 sur heures hautes mesurées : H={Hhm:.4f} ; {Hhm*4*1.38+4:.4f} -> {5*math.ceil((Hhm*4*1.38+4)/5)}")
# Moment de l'arrêt de la coupe (A14) : honnête d'abord, sans terme d'adaptation (dose 0)
tb = h(mer_s) + h(2304*2.1) + ident + h(128*d)
th = 1.0 + h(2304*3.0) + ident + h(128*42.8)
print(f"A14 tombe à {tb:.2f} à {th:.2f} h ; dépensé {tb*1.1833333+fixes:.2f} à {th*1.30+2:.2f} USD")
# Échéance de la machine
print(f"échéance : 2 x H2 = {2*H2(d):.2f} h -> {math.ceil(2*H2(d))} h ; heure du plafond P=44 : {(44-fixes)/1.1833333-0.5:.2f} h")
# Crédit
print(f"crédit : 56.365824 - 2.83 - 0.20 = {56.365824434155-2.83-0.20:.2f}")
# Ligne 1 réelle
print(f"ligne 1 : {cumul:.2f} au compteur ; 2.83 + 0.20 = {2.83+0.20:.2f}")
# Offres du relevé de 04:45Z, disque 150 Go : stockage = coût Go/mois x 150 / 720
for i, b, s, t in ((60992138,1.0533333,1.0,0.0390625),(61615835,1.0573333,1.0,0.0390625),(29019350,1.1333333,0.24,0.0260417),
                   (53645770,1.1733333,0.3466667,0.0133333),(34475474,1.1866667,0.24,0.0026042),(29296811,1.1866667,0.24,0.0260417),
                   (36695163,1.2533333,0.2,0.0026042),(59306791,1.738,0.6998653,0.0133333),(41153679,1.8093333,0.3333333,0.004)):
    st = s*150/720
    ok = b <= 1.30 and st <= 0.08 and t <= 0.05
    print(f"  {i} carte {b:.4f} stockage {st:.4f} total {b+st:.4f} tél {t:.4f} 40Go {40*t:.2f} {'SOUS' if ok else 'hors'}")
# Ensemble
print(f"total carte : ligne 1 {2.83+0.20:.2f} + ligne 2 {Ab:.1f} à {Ah:.1f} = {3.03+Ab:.1f} à {3.03+Ah:.1f}")
print(f"plafonds : 18 + 44 + 670 = {18+44+670}")
