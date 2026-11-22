import os, tempfile, json
from controle_ia.oracles_plantes_v1.parametres import charger
from controle_ia.oracles_plantes_v1.banque import construire_mondes
from controle_ia.oracles_plantes_v1.tests_de_mort import appliquer_batterie, sortie_de_texte, t5_redite
from controle_ia.oracles_plantes_v1.normalisation import normaliser
from controle_ia.oracles_plantes_v1.lignee import Registre, rejouer
from controle_ia.oracles_plantes_v1.cles import octets_json, verifier_absence_fuite
p,_ = charger()
ms = construire_mondes(11, p)
f3 = ms[8]
def fo(t): return normaliser(f3.analyser(t), f3, f3.ev)
a = "pour tout n dans NAT, n >= 1 implique mod(w(30 * n), w(n)) = 0"
b = "pour tout n dans NAT, n >= 1 implique mod(w(30 * n), w(3 * n)) = 0"
for t in (a,b):
    r = appliquer_batterie(sortie_de_texte(t), f3)
    print(t, r.statut, r.vraie_bornee, r.triviale, [(i.test, i.type.value) for i in r.issues])
iss = t5_redite(fo(b), f3, [fo(a)])
print("T5 b vs a:", iss.type.value, iss.motif)
# registre : troncature / modification de la dernière ligne
d = tempfile.mkdtemp(); ch = os.path.join(d, "l.jsonl")
reg = Registre(ch)
reg.inscrire("a"*64, "vivante", "batterie", "x")
reg.inscrire("a"*64, "morte", "T6", "contre-exemple vérifié")
lignes = open(ch).read().splitlines()
open(ch, "w").write(lignes[0] + "\n")
print("après troncature de la dernière ligne :", rejouer(ch))
open(ch, "w").write(lignes[0] + "\n" + lignes[1].replace('"morte"', '"vivante"') + "\n")
print("après modification de la dernière ligne :", rejouer(ch))
# fuite d'instance en JSON indenté
servi = octets_json({"items": [{"instance": {"n": 17}}]})
try:
    verifier_absence_fuite(servi, [json.dumps({"n": 17}, ensure_ascii=False, sort_keys=True)])
    print("instance fuitée NON détectée")
except Exception as e:
    print("détectée", e)
