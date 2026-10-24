"""Organisme factice : apprentissage minimal, pour tester le noyau. Jamais donné à l'essaim réel."""
import json, os, shutil, time

import noyau_client as nc

ICI = os.path.dirname(os.path.abspath(__file__))


def _lire_connaissances():
    with open(os.path.join(ICI, "connaissances.json"), encoding="utf-8") as fh:
        return json.load(fh)


def _json(texte):
    if "```json" in (texte or ""):
        morceau = texte.split("```json", 1)[1].split("```", 1)[0]
        try:
            return json.loads(morceau)
        except json.JSONDecodeError:
            return None
    return None


def _apprendre(contexte, connaissances, journal, budget):
    """Découverte par une espèce, vérification par une autre ; garde ce qui est VALIDE."""
    especes = nc.especes()
    positifs = [t for t in contexte["taches_entrainement"] if t["verite"] == t["etiquettes"][0]]
    if not positifs or budget["appels"] < 2:
        return
    fermes = [e["enonce"] for e in connaissances["entrees"]]
    for famille in sorted({t["famille"] for t in positifs}):
        if budget["appels"] < 2:
            break
        exemples = [t for t in positifs if t["famille"] == famille][:8]
        contexte_txt = "\n".join(f"- [{t['id']}] (vérité : {t['verite']}) {t['texte']}" for t in exemples)
        prompt = ("Tu es un attaquant de l'étage M1 (découverte). Propose des indices.\n\n"
                  f"CIBLE : indices pour {famille}\n\nCONTEXTE :\n{contexte_txt}\n\n"
                  "DÉJÀ FERMÉ (ne répète pas) :\n" + "\n".join(f"- {x}" for x in fermes) + "\n\n"
                  "Termine par un bloc ```json {\"candidats\": [{\"enonce\": \"…\", \"confiance\": 0.0}]} ```")
        r = nc.appeler(especes[0], prompt, role="decouverte")
        budget["appels"] -= 1
        journal.append({"etape": "decouverte", "famille": famille, "statut": r["statut"]})
        d = _json(r["texte"]) if r["statut"] == "OK" else None
        candidats = [c["enonce"] for c in (d or {}).get("candidats", []) if isinstance(c, dict) and c.get("enonce")]
        if not candidats or budget["appels"] < 1:
            continue
        items = "\n".join(f"[item-{i+1:02d}] {c}" for i, c in enumerate(candidats))
        prompt_v = ("Tu es un vérificateur isolé de l'étage M1. Juge chaque item VALIDE ou INVALIDE.\n\n"
                    f"CONTEXTE :\n{contexte_txt}\n\nITEMS :\n{items}\n\n"
                    "Termine par un bloc ```json {\"verdicts\": {\"item-01\": \"VALIDE\"}} ```")
        rv = nc.appeler(especes[-1], prompt_v, role="verification")
        budget["appels"] -= 1
        journal.append({"etape": "verification", "famille": famille, "statut": rv["statut"]})
        verdicts = (_json(rv["texte"]) or {}).get("verdicts", {}) if rv["statut"] == "OK" else {}
        for i, c in enumerate(candidats):
            if verdicts.get(f"item-{i+1:02d}") == "VALIDE" and c not in fermes:
                connaissances["entrees"].append({"id": f"C-{len(connaissances['entrees'])+1:04d}", "enonce": c,
                                                 "generation": contexte["generation"], "famille": famille})
                fermes.append(c)


def _repondre(contexte, taches, connaissances, journal, budget):
    especes = nc.especes()
    reponses = {}
    conn = "\n".join(f"- [{e['id']}] {e['enonce']}" for e in connaissances["entrees"]) or "- (aucune)"
    for i, t in enumerate(taches):
        if budget["appels"] < 1:
            break
        prompt = (f"Tâche de la famille « {t['famille']} ». Choisis une étiquette parmi {t['etiquettes']}.\n\n"
                  f"EXTRAIT :\n{t['texte']}\n\nCONNAISSANCES DE L'ESSAIM :\n{conn}\n\n"
                  "Réponds par un bloc ```json {\"etiquette\": \"…\", \"confiance\": 0.0} ```")
        r = nc.appeler(especes[i % len(especes)], prompt, role="tache")
        budget["appels"] -= 1
        d = _json(r["texte"]) if r["statut"] == "OK" else None
        if d and d.get("etiquette") in t["etiquettes"]:
            reponses[t["id"]] = {"etiquette": d["etiquette"], "confiance": float(d.get("confiance", 0.5))}
    journal.append({"etape": "reponses", "n": len(reponses), "sur": len(taches)})
    return reponses


def executer(contexte):
    debut = time.time()
    travail = contexte["dossier_travail"]
    budget = {"appels": int(contexte["budget"]["appels_max"])}
    connaissances = _lire_connaissances()
    journal = [{"etape": "debut", "generation": contexte["generation"], "historique": contexte["historique"]}]
    _apprendre(contexte, connaissances, journal, budget)
    reponses = _repondre(contexte, contexte["taches_test"], connaissances, journal, budget)
    with open(os.path.join(travail, "reponses_test.json"), "w", encoding="utf-8") as fh:
        json.dump(reponses, fh, ensure_ascii=False)
    # successeur : copie de soi-même avec la mémoire mise à jour
    succ = os.path.join(travail, "successeur", "organisme")
    shutil.copytree(ICI, succ, ignore=shutil.ignore_patterns("__pycache__"))
    with open(os.path.join(succ, "connaissances.json"), "w", encoding="utf-8") as fh:
        json.dump(connaissances, fh, ensure_ascii=False, indent=1)
    journal.append({"etape": "fin", "duree_s": round(time.time() - debut, 2), "n_connaissances": len(connaissances["entrees"]),
                    "appels_restants": budget["appels"], "budget_noyau": nc.budget()})
    with open(os.path.join(travail, "journal-organisme.json"), "w", encoding="utf-8") as fh:
        json.dump(journal, fh, ensure_ascii=False, indent=1)
    return f"{len(reponses)} réponses, {len(connaissances['entrees'])} connaissances"
