"""Charge toutes les cellules (tous tours) des courses incluses, avec lettre, espèce, tour, rôle.

Sert aux mesures. Cache local dans le bloc-notes de la session si la variable AUDIT_CACHE est posée ;
sinon relu par git à chaque appel.
"""
import json
import os
import pickle
import re

from audit_commun_v2 import inventaire, lister, montrer, ESPECE_FOURNISSEUR


def role(nom):
    if "conception" in nom:
        return "conception"
    if "critique" in nom:
        return "critique"
    if "reponse" in nom or "réponse" in nom:
        return "reponse"
    return "autre"


def charger():
    cache = os.environ.get("AUDIT_CACHE")
    if cache and os.path.exists(cache):
        return pickle.load(open(cache, "rb"))
    out = []
    for d in inventaire():
        if d.get("type") != "course" or d["statut_audit"] != "inclus":
            continue
        for f in lister(d["branche"], d["racine"] + "/"):
            if not re.search(r"/cellules/[^/]+\.md$", f):
                continue  # les copies d'abonnement doublent les cellules : on ne garde que cellules/
            nom = f.rsplit("/", 1)[1]
            m = re.search(r"-([A-Z])\.md$", nom)
            t = re.search(r"T(\d)", nom)
            if not m or not t:
                continue
            L = m.group(1)
            esp = (d["lettres"].get(L) or {}).get("espece", "inconnu")
            out.append({"racine": d["racine"], "rejeu_de": d.get("rejeu_de"), "branche": d["branche"],
                        "commit": d["commit"], "chemin": f, "lettre": L, "espece": esp,
                        "fournisseur": ESPECE_FOURNISSEUR.get(esp, "autre"), "tour": int(t.group(1)),
                        "role": role(nom), "texte": montrer(d["branche"], f) or "",
                        "lettres_course": {k: v.get("espece") for k, v in d["lettres"].items()}})
    if cache:
        pickle.dump(out, open(cache, "wb"))
    return out
