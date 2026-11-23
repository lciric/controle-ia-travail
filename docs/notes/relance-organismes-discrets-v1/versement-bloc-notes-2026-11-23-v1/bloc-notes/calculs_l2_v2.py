# Complément de devis, ligne 2 du bras A : calculs (bibliothèque standard).
import math
h = lambda s: s / 3600
d, mer, pu = 4596.4681555219995 / 128, h(243.31626677513123), 50.73237615299513 / 128   # manifeste, clé resume
queue = (2.83 - 2.6325220931095106) / 1.1833333333333333                                  # mandat : 2,83 au plus
fixes = 1.0416666666666667
ident = 0.30
print(f"d={d:.4f} mer={mer:.4f} pu={pu:.4f} queue={queue:.4f} h")
# Attendu (règle 3.3 du devis v5)
Hb = mer + h(2304*2.1) + ident + h(896*d) + h(1280*pu) + queue
Hh = 1.0 + h(2304*3.0) + ident + h(896*42.8) + h(1280*0.45) + queue
print(f"heures bas {Hb:.4f} ; haut {Hh:.4f}")
print(f"attendu bas {Hb*1.1833333333333333+fixes:.4f} ; haut {Hh*1.30+2.0:.4f}")
# Plafonds
k = 1.0 + ident + h(2304*6.0) + h(1280*0.90)       # max(1,0 ; m) = 1,0
Ha = k + h(896*d)
Hbb = k + h(128*d) + h(768*42.8)
Pa, Pb = 2*1.38*Ha + 4, 2*1.38*Hbb + 4
print(f"(a) H2={Ha:.4f} P={Pa:.4f} -> {math.ceil(Pa)} ; (b) H2={Hbb:.4f} P={Pb:.4f} -> {math.ceil(Pb)}")
Hc = 1.0 + h(2304*3.0) + ident + h(896*d) + h(1280*0.45)
Pc = Hc*4*1.38 + 4
print(f"(c) H={Hc:.4f} P={Pc:.4f} -> {5*math.ceil(Pc/5)}")
# Tolérance : durée des 768 épisodes à adaptateur, honnête mesuré, une relance complète au prix maximal
for P in (44, 48, 75):
    t = ((P - 4)/2.76 - k - h(128*d)) * 3600 / 768
    t1 = ((P - 2)/1.38 - k - h(128*d)) * 3600 / 768
    t2 = (((P - 2*fixes)/2)/1.1833333333333333 - k - h(128*d)) * 3600 / 768
    print(f"P={P} : relance au prix max {t:.2f} s ; sans relance au prix max {t1:.2f} s ; relance au tarif du jour {t2:.2f} s")
# Échéance et heure du plafond
ech = math.ceil(2*Hh)
print(f"échéance création + {ech} h ({2*Hh:.2f})")
for P in (44, 48, 75):
    print(f"P={P}: heure du plafond {(P-fixes)/1.1833333333333333-0.5:.2f} h (jour) ; {(P-2)/1.38-0.5:.2f} h (max) ; coût à l'échéance au max {ech*1.38+2:.2f}")
# Crédit
cr = 56.365824434155 - 2.83 - 0.20
print(f"crédit restant {cr:.2f} ; recharge pour 75 : {75+2-cr:.2f}")
# Coupe A14 : moment
tb = mer + h(2304*2.1) + ident + h(128*d); th = 1.0 + h(2304*3.0) + ident + h(128*42.8)
print(f"A14 à {tb:.2f}-{th:.2f} h ; dépensé {tb*1.1833333+fixes:.2f}-{th*1.30+2:.2f}")
# Totaux de la course
for a in (Hb*1.1833333333333333+fixes, Hh*1.30+2.0):
    print(f"course : {3.03 + a + 255:.1f}")
print(f"ligne 1 compteur {2.6325220931095106:.4f} = {fixes:.4f} + {(2.6325220931095106-fixes)/1.1833333333333333:.4f} h x 1,1833 ; création->fin {4840/3600:.4f} h")
print(f"passes/pas de lot {53912/160:.2f} ; ms/passe {1000*4542.726181091997/53912:.2f} ; jetons/action {292813/1280:.2f} ; ctx/action {3202584/1280:.0f} ; transcription {538098/128:.1f}")
