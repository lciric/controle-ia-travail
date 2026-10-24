"""Organisme factice « sonde » : conçoit une perte, entraîne par gradient via le noyau, répond. Test seulement."""
import json, os, shutil

import noyau_client as nc

ICI = os.path.dirname(os.path.abspath(__file__))
PERTE_BRIER = "def perte(p, y):\n    return float(((p - y) ** 2).mean())\n"


def _etat():
    chemin = os.path.join(ICI, "etat.json")
    if os.path.exists(chemin):
        with open(chemin, encoding="utf-8") as fh:
            return json.load(fh)
    return {"pas": 800, "taux": 2.0, "seuil_indecision": 0.15}


def executer(contexte):
    travail = contexte["dossier_travail"]
    etat = _etat()
    hist = contexte.get("historique") or []
    if len(hist) >= 2 and hist[-1]["score"] is not None and hist[-2]["score"] is not None and hist[-1]["score"] < hist[-2]["score"]:
        etat["pas"] = min(int(etat["pas"] * 1.5), int(contexte["budget"].get("pas_max", 5000)))
    reponses, journal = {}, {"entrainement": None, "appels": 0, "par_sonde": 0, "par_espece": 0}
    train = contexte["taches_entrainement"]
    modele = None
    if contexte.get("traits", {}).get("disponibles") and contexte["budget"].get("entrainements_max", 0) > 0:
        spec = {"donnees": [t["id"] for t in train], "objectif": PERTE_BRIER,
                "algorithme": {"type": "sonde-lineaire", "pas": int(etat["pas"]), "taux": float(etat["taux"]), "l2": 0.001, "lot": 40, "graine": 7},
                "pretraitement": {"normaliser": True}}
        r = nc.entrainer(spec, role="sonde-brier")
        journal["entrainement"] = {k: r.get(k) for k in ("statut", "identifiant", "exactitude_entrainement", "perte_finale_entrainement", "problemes", "echec")}
        if r.get("statut") == "OK":
            modele = r["identifiant"]
    probas = {}
    if modele:
        pr = nc.predire(modele, [t["id"] for t in contexte["taches_test"]], role="sonde-test")
        if pr.get("statut") == "OK":
            probas = pr["probabilites"]
    especes = nc.especes()
    for t in contexte["taches_test"]:
        p = probas.get(t["id"])
        pos, neg = t["etiquettes"][0], t["etiquettes"][1]
        if p is not None and abs(p - 0.5) >= etat["seuil_indecision"]:
            reponses[t["id"]] = {"etiquette": pos if p >= 0.5 else neg, "confiance": round(max(p, 1 - p), 4)}
            journal["par_sonde"] += 1
            continue
        if nc.budget()["appels_restants"] <= 0:
            continue
        prompt = (f"Tâche de la famille « {t['famille']} ». Lis l'extrait et choisis une étiquette parmi {t['etiquettes']}.\n\n"
                  f"EXTRAIT :\n{t['texte']}\n\nCONNAISSANCES :\n- (aucune)\n\nRéponds par un bloc ```json {{\"etiquette\": \"…\", \"confiance\": 0.0}} ```.")
        r = nc.appeler(especes[0], prompt, role="tache")
        journal["appels"] += 1
        if r.get("statut") == "OK" and "```json" in r["texte"]:
            try:
                d = json.loads(r["texte"].split("```json", 1)[1].split("```", 1)[0])
                if d.get("etiquette") in t["etiquettes"]:
                    reponses[t["id"]] = {"etiquette": d["etiquette"], "confiance": float(d.get("confiance", 0.5))}
                    journal["par_espece"] += 1
            except (json.JSONDecodeError, ValueError):
                pass
    with open(os.path.join(travail, "reponses_test.json"), "w", encoding="utf-8") as fh:
        json.dump(reponses, fh, ensure_ascii=False)
    with open(os.path.join(travail, "journal_organisme.json"), "w", encoding="utf-8") as fh:
        json.dump({"etat": etat, **journal}, fh, ensure_ascii=False)
    with open(os.path.join(travail, "metrique_proposee.json"), "w", encoding="utf-8") as fh:
        json.dump({"nom": "exactitude_entrainement_sonde", "definition": "exactitude de la sonde sur ses propres données d'entraînement (indice descriptif)",
                   "valeur": (journal["entrainement"] or {}).get("exactitude_entrainement"), "justification": "test"}, fh, ensure_ascii=False)
    succ = os.path.join(travail, "successeur", "organisme")
    shutil.copytree(ICI, succ, ignore=shutil.ignore_patterns("__pycache__"))
    with open(os.path.join(succ, "etat.json"), "w", encoding="utf-8") as fh:
        json.dump(etat, fh)
    return f"{len(reponses)} réponses ; sonde={journal['par_sonde']} ; espèce={journal['par_espece']}"
