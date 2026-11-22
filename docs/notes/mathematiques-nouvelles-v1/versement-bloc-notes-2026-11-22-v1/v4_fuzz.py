import os, tempfile, json, random, sys, traceback
from controle_ia.oracles_plantes_v4.parametres import charger
from controle_ia.oracles_plantes_v4.banque import construire_banque
from controle_ia.oracles_plantes_v4.tests_de_mort import appliquer_batterie, sortie_de_texte, appliquer_t6
from controle_ia.oracles_plantes_v4.lignee import Registre
from controle_ia.oracles_plantes_v4 import base_aleatoire
p,_ = charger()
banque = construire_banque(3, p)
rnd = random.Random(int(sys.argv[1]))
TOK = [" + 1", " * 0", " - n", "^16", "^600", " / 0", " / (n - n)", ")", "(", " et vrai", " ou faux", " 9"*3, "99999999999999999999999999999999999999999999999999", "^(-1)", " * (n + 1)^16", "0.5", "1e999", "mod(", "somme(k, 0, 100000, k)", "fact(300)", "binom(300, 150)", "u(n * 1000)", "vt(n + 100)", "[0 .. n]", "pour tout k dans [0 .. 1000], "]
ex = {}
morts_verites = 0
for (m, plantes) in banque:
    R = Registre(os.path.join(tempfile.mkdtemp(), "r.jsonl"))
    textes = [x.texte for x in plantes]
    for _ in range(int(sys.argv[2])):
        t = rnd.choice(textes)
        for _ in range(rnd.randint(1, 4)):
            i = rnd.randint(0, len(t)); t = t[:i] + rnd.choice(TOK) + t[i:]
        if rnd.random() < 0.3:
            t = f"pour tout n dans NAT, ({rnd.choice(textes).split(', ',1)[-1]}) et ({t.split(', ',1)[-1]})"
        try:
            appliquer_batterie(sortie_de_texte(t), m, registre=R)
        except Exception as e:
            k = type(e).__name__ + ":" + str(e)[:60]
            ex.setdefault(k, t)
    for x in plantes:
        try:
            r = appliquer_batterie(sortie_de_texte(x.texte), m, registre=R)
            if x.etiquette == "VERITE_PLANTEE" and (r.statut != "vivante" or not r.vraie_bornee): morts_verites += 1; print("VERITE", r.statut, x.texte)
        except Exception as e:
            print("ARRET sur planté", x.etiquette, type(e).__name__, e)
print("exceptions distinctes:", len(ex)); 
for k, t in list(ex.items())[:15]: print(" ", k, "|", t[:150])
print("vérités mortes ou non vraies-bornées:", morts_verites)
