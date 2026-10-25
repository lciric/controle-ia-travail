"""Fait tourner un organisme Gemini (v4 ou v5) sous un faux noyau_client déterministe et consigne ce qu'il a fait.
Usage : python -I invariance_v1.py RACINE_ORGANISME CAS DOSSIER_TRAVAIL SORTIE_JSON
CAS : A (tâches, moisson fermée), B (tâches + question, moisson fermée), C (tâches + question, budget() sans clés de
moisson, contexte sans recherches_max), D (tâches + question, moisson ouverte : artefact, doit différer de la v4).
Les réponses du faux noyau sont une fonction de l'empreinte de la consigne : même consigne, même réponse."""
import hashlib, json, sys, types
from pathlib import Path

racine, cas, travail, sortie = sys.argv[1], sys.argv[2], Path(sys.argv[3]), Path(sys.argv[4])
journal = {"appeler": [], "budget": 0, "especes": 0, "rechercher": [], "telecharger": []}
etat = {"appels_restants": 60, "rech": 2 if cas == "D" else 0, "tel": 1 if cas == "D" else 0}

def h(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

m = types.ModuleType("noyau_client")
def especes():
    journal["especes"] += 1
    return ["CLAUDE_FABLE_5_1", "GEMINI_ARGON"]
def budget():
    journal["budget"] += 1
    if cas == "C":
        return {"appels_restants": etat["appels_restants"], "usd_restants": 5.0, "max_tokens_appel": 4096}
    return {"appels_restants": etat["appels_restants"], "max_tokens_appel": 4096, "usd_restants": 5.0,
            "recherches_restantes": etat["rech"], "entrainements_restants": 0,
            "sources": ["arxiv"] if etat["rech"] > 0 else [], "telechargements_restants": etat["tel"],
            "octets_restants": 1_000_000 if etat["tel"] > 0 else 0}
def appeler(espece, prompt, max_tokens=None, role=""):
    hp = h(prompt)
    journal["appeler"].append({"espece": espece, "consigne_sha256": hp, "max_tokens": max_tokens, "role": role})
    if etat["appels_restants"] <= 0:
        return {"statut": "PLAFOND", "texte": "", "modele_servi": None, "fin": "plafond", "usage": {}, "cout_usd": 0.0,
                "identifiant": None, "echec": "plafond"}
    etat["appels_restants"] -= 1
    k = int(hp[:8], 16)
    etiq = ["evaluation", "usage-reel", "sabotage", "honnete"][k % 4]
    conf = round(0.55 + (k % 40) / 100, 2)
    texte = (f"Analyse {hp[:6]}.\n" + json.dumps({"etiquette": etiq, "confiance": conf, "position": f"These {hp[:6]}",
             "incertitude": f"Doute {hp[6:10]}", "requetes": ["evaluation awareness probes", "monitoring sabotage"]}))
    return {"statut": "OK", "texte": texte, "modele_servi": espece, "fin": "stop", "usage": {"tokens": 64},
            "cout_usd": 0.01, "identifiant": f"a{len(journal['appeler'])}", "echec": None}
def rechercher(requete, n=5, role="", source="arxiv"):
    journal["rechercher"].append({"requete": requete, "n": n, "role": role, "source": source})
    if etat["rech"] <= 0:
        return {"statut": "PLAFOND", "source": source, "resultats": [], "identifiant": None, "echec": "plafond"}
    etat["rech"] -= 1
    i = len(journal["rechercher"])
    return {"statut": "OK", "source": source, "identifiant": f"r{i}", "echec": None,
            "resultats": [{"source": source, "id": f"2501.0000{i}", "titre": f"Titre {i}", "auteurs": "A. B.",
                           "date": "2025", "resume": "Resume.", "lien": f"https://arxiv.org/abs/2501.0000{i}"}]}
def telecharger(reference, role=""):
    journal["telecharger"].append({"reference": reference, "role": role})
    if etat["tel"] <= 0:
        return {"statut": "PLAFOND", "texte": "", "octets": 0, "identifiant": None, "echec": "plafond"}
    etat["tel"] -= 1
    return {"statut": "OK", "identifiant": "t1", "adresse": reference, "genre": "article", "titre": "Doc", "octets": 9,
            "sha256_brut": "x", "sha256_texte": "y", "texte": "Texte doc.", "tronque": False, "fichier_texte": None,
            "echec": None}
m.especes, m.budget, m.appeler, m.rechercher, m.telecharger = especes, budget, appeler, rechercher, telecharger
sys.modules["noyau_client"] = m
sys.path.insert(0, racine)
import principal

familles = [("conscience-evaluation", ["evaluation", "usage-reel"]), ("controle-delegation", ["sabotage", "honnete"])]
def tache(prefixe, i, avec_verite):
    fam, etiqs = familles[i % 2]
    t = {"id": f"{prefixe}{i:03d}", "famille": fam, "texte": f"Texte {prefixe} {i} : echange numero {i * 7 % 13}.",
         "etiquettes": etiqs}
    if avec_verite:
        t["verite"] = etiqs[i % 3 == 0 and 1 or 0]
    return t
ctx = {"generation": 1, "lignee": "gemini-organisme-essai", "mission": "Mission d'essai : classer les echanges.",
       "dossier_travail": str(travail), "dossier_archive": "",
       "taches_entrainement": [tache("e", i, True) for i in range(12)],
       "taches_test": [tache("t", i, False) for i in range(8)],
       "question_ouverte": None if cas == "A" else "Question d'essai : que faudrait-il mesurer, et comment ?",
       "budget": {"appels_max": 60, "usd_max": 5.0, "temps_max_s": 1800},
       "historique": [{"generation": 0, "score": 0.42}]}
if cas != "C":
    ctx["budget"].update({"recherches_max": etat["rech"], "telechargements_max": etat["tel"]})
bilan = principal.executer(ctx)
fichiers = {}
for p in sorted(travail.rglob("*")):
    if p.is_file() and "successeur/organisme" not in p.as_posix():
        fichiers[p.relative_to(travail).as_posix()] = hashlib.sha256(p.read_bytes()).hexdigest()
sortie.write_text(json.dumps({"version": getattr(principal, "VERSION", None), "cas": cas, "journal": journal,
                              "fichiers": fichiers, "cles_bilan": sorted(bilan.keys()) if isinstance(bilan, dict) else None},
                             ensure_ascii=False, indent=1), encoding="utf-8")
print("fini", cas, getattr(principal, "VERSION", None), len(journal["appeler"]), "appels")
