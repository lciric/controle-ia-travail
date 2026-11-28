"""Mémoire de pointe d'une passe unique du modèle jouet de P3 sur l'ouverture d'une tâche (tokeniseur par caractères),
sous un noyau d'attention donné. Lancé depuis la racine du dépôt de travail (lecture seule), PYTHONPATH=src.
Usage : mesure_passe.py NOYAU INDICE_TACHE CONDITION"""
import json
import resource
import sys
import time

import torch

from controle_ia.environnements.invites import charger_invite
from controle_ia.environnements.lancer_pilote_a import charger_modele_et_format
from controle_ia.environnements.pilote_a import charger_taches, tache_de
from controle_ia.harnais.activations import passe_unique
from controle_ia.harnais.validation_reelle import noyau
from controle_ia.premier_test_ia.conditions import charger_consignes, environnement

nom_noyau, indice, condition = sys.argv[1], int(sys.argv[2]), sys.argv[3]
torch.set_num_threads(4)
taches = charger_taches("donnees/t05-pilote-v1/taches-pilote-60-v1.json")
consignes = charger_consignes("brouillons/P3-consignes-v1-candidat2.md",
                              "a68468fef6286bbcaa31451ba461d0adab2af7d529dd5e4fa0695643e6d1d69c")
guide = charger_invite("H1-classification")
modele, fmt = charger_modele_et_format({"nom": "agent-jouet"}, "jouet", 12345)
env = environnement(condition, tache_de(taches[indice]), 2, guide, consignes)
ids = fmt.ouverture(env.consigne_privee(0), env.observation(0, 0, []))
avant = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
debut = time.perf_counter()
with noyau(nom_noyau):
    acts = passe_unique(modele, ids, [0, 2])
duree = time.perf_counter() - debut
pointe = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
print(json.dumps({"noyau": nom_noyau, "tache": indice, "identifiant": taches[indice]["identifiant"], "condition": condition,
                  "jetons": len(ids), "pointe_avant_mo": round(avant / 1024), "pointe_mo": round(pointe / 1024),
                  "duree_s": round(duree, 1)}, ensure_ascii=False))
