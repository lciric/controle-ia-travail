"""Banc : calcule, par une voie indépendante de l'outil (reconstruction directe, sans ses contrôles), la taille et
l'empreinte du corps de création attendu pour un fichier de données ; n'écrit ni n'affiche le corps.
Emploi : python -I corps-attendu.py DONNEES
"""
import hashlib
import json
import sys

texte = open(sys.argv[1], "rb").read().decode("ascii")
corps = {"name": "essai-3-palier-0b", "server_type": "cpx42", "location": "hel1", "image": "debian-13",
         "user_data": texte, "public_net": {"enable_ipv4": True, "enable_ipv6": True},
         "start_after_create": True, "ssh_keys": []}
b = json.dumps(corps, ensure_ascii=True).encode("ascii")
print("corps attendu : %d octets, sha256 %s" % (len(b), hashlib.sha256(b).hexdigest()))
