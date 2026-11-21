"""Sondage indépendant de chiffres du devis v5 (contre-lecture 1). Processeur seulement."""
from math import floor, ceil
P_reel, P_max = 1.186667 + 0.033333, 1.30 + 0.08
ep, act = 3439 / 88, 491 / 960
fixe = 320 + (543 - 8 * ep)
print(f"S01 épisode {ep:.2f} s ; action d'oracle {act:.3f} s ; fixe {fixe:.0f} s")
etal = fixe + 160 * ep + 3840 * act
print(f"S02 étalonnage attendu {etal/3600:.2f} h, {etal/3600*P_reel:.2f} USD")
print(f"S03 comptes : étalonnage 640*5+320*2 = {640*5+320*2} ; 12 tours (b') {3840+12*320+2560+3520} ; 24 tours {3840+24*320+2560+3520}")
print(f"S04 épisodes 12 tours {160+12*32+256} ; 24 tours {160+24*32+256}")
tour = 32 * (ep + 10 * act)
print(f"S05 un tour attendu {tour:.0f} s, {tour/3600*P_reel:.3f} USD")
fc = 256 * ep + 2560 * act + 2 * 96 * 3 * 891 / 480 + 36 + 360
print(f"S06 coût fixe attendu {fc/3600:.2f} h, {fc/3600*P_reel:.2f} USD (+2 téléchargement = {fc/3600*P_reel+2:.2f})")
ht = 3520 * act
def rplaf(pl, e=etal, t=tour, f=fc, a=ht, p=P_reel):
    return floor((pl - e/3600*p - (f/3600*p + 2) - a/3600*p) / (t/3600*p))
print(f"S07 R_plafond attendu à 50 : {rplaf(50)} ; à 55 : {rplaf(55)} ; à 45 : {rplaf(45)} ; à 40 : {rplaf(40)}")
print(f"S08 gardes : 55 + {2400/3600*P_max:.2f} + {48*0.08:.2f} = {55+2400/3600*P_max+48*0.08:.2f}")
print(f"S09 coupure 55 : {(55-2)/P_reel:.1f} h au prix réel ; {(55-2)/P_max:.1f} h à la borne")
print(f"S10 dépense première course : {(4835.89+7)*P_reel/3600 + 382*0.033333/3600:.2f} USD")
# tolérance à un dépassement des tours (épisodes du maître plus lents que l'honnête mesuré à l'étalonnage)
for pl in (50, 45, 40):
    r = rplaf(pl)
    base = (etal + r * tour + fc + ht) / 3600 * P_reel + 2
    marge = 55 - base
    tol = marge / (r * tour / 3600 * P_reel)
    kmin = next(k for k in range(1, 65) if ceil(384 / k) <= r)
    print(f"S11 fichier {pl} : {r} tours au plus ; dépense planifiée {base:.2f} USD ; marge sous la coupure {marge:.2f} ; "
          f"les tours peuvent être {100*tol:.0f} % plus lents que mesurés avant la coupure ; k_R ≥ {kmin}")
print("S12 10.3 étape 7 : R ≤ 12 part à la taille d'origine (12 tours) : 6 tours n'est pas une configuration possible")
