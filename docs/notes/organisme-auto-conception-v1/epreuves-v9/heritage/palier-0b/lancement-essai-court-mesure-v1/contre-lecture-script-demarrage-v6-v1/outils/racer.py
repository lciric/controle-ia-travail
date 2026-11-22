"""Course de remplacement atomique sur la copie privee de l'amorce.
Usage : python -I racer.py PREFIXE_CHARGE BON.sh FAUX.sh STOP
Attend un dossier PREFIXE_CHARGE.script.* avec s.sh, puis alterne en boucle bon/faux par os.replace (fichier neuf a chaque fois,
jamais d'ecriture dans le fichier de l'amorce) jusqu'a l'apparition du fichier STOP."""
import glob, os, sys, time
pref, bon, faux, stop = sys.argv[1:5]
B = open(bon, "rb").read()
F = open(faux, "rb").read()
open(stop + ".ready", "w").close()
t0 = time.time()
cible = None
while not os.path.exists(stop) and time.time() - t0 < 20:
    g = glob.glob(pref + ".script.*/s.sh")
    if g:
        cible = g[0]
        break
d = os.path.dirname(cible) if cible else None
n = 0
if cible:
    tmp = os.path.join(d, "t.tmp")
    cur = 0
    while True:
        n += 1
        if n % 2000 == 0 and os.path.exists(stop):
            break
        try:
            with open(tmp, "wb") as f:
                f.write(F if cur else B)
            os.replace(tmp, cible)
            cur ^= 1
        except OSError:
            if os.path.exists(stop):
                break
print("racer: iterations", n, file=sys.stderr)
