# Valide la configuration A v2 seule avec valider_configuration du masque v2 (copie verifiee) ; aucune carte.
import hashlib
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import masque_style_cartes_v1 as M1
import masque_style_cartes_v2 as M2

CONF = "/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/rejeu-masque-lecteur-v1/configuration-a-v2/configuration-a-masque-v2.json"
ATTENDU = "a6c5d87bf73ebcae10ff7cf87390dd4827431ce0480bbf008df755d59b3b7f54"

with open(os.path.join(ICI, "masque_style_cartes_v2.py"), "rb") as f:
    print("sha masque v2 copie :", hashlib.sha256(f.read()).hexdigest())
with open(CONF, "rb") as f:
    octets = f.read()
print("sha configuration :", hashlib.sha256(octets).hexdigest(), "attendue egale :", hashlib.sha256(octets).hexdigest() == ATTENDU)
conf = json.loads(octets.decode("utf-8"))
try:
    M2.valider_configuration(conf)
    print("v2 valider_configuration : PASSE")
except M2.Refus as e:
    print("v2 REFUS :", e)
try:
    M1.valider_configuration(json.loads(octets.decode("utf-8")))
    print("v1 : passe (inattendu)")
except M1.Refus as e:
    print("v1 REFUS (attendu) :", e)
