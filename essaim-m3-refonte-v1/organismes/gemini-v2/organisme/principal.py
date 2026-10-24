"""Organisme « essaim de Gemini, v2 déboguée » sous le contrat du noyau.

Conception conservée (celle des scripts du dossier 17, telle que `m3_commun` la rend honnête) : des castes
(mode, lignées, température) postent sur un tableau partagé ; des sondes d'écart (« M2 ») s'éloignent des structures
fréquentes ; un arbitre extrait un JSON (« M1 ») ; une synthèse (« M0 ») répond. Ce qui change : les appels passent
par le noyau (journal, plafonds, aucune bascule de modèle), et l'organisme répond aux tâches cachées du juge externe,
mémorise ce qu'il extrait dans son substrat, et se recopie en successeur. Il propose comme métrique la « capacité de
Shannon-Gram » de son tableau, nom repris des scripts d'origine (indice descriptif de diversité, sans portée théorique).

Rien ici n'est opposable : les « indices » extraits sont du texte de modèle, non vérifiés (statut `non-verifie`).
"""
import json
import os
import shutil
from pathlib import Path

import m3_commun as m3
from adaptateur_noyau import ClientNoyau

ICI = Path(__file__).resolve().parent


def prompt_tache(t: dict, connaissances: list) -> str:
    conn = "\n".join(f"- [{c['id']}] {c['enonce']}" for c in connaissances) or "- (aucune)"
    return (f"Tâche de la famille « {t['famille']} ». Lis l'extrait et choisis une étiquette parmi {t['etiquettes']}.\n\n"
            f"EXTRAIT :\n{t['texte']}\n\nCONNAISSANCES DE L'ESSAIM (cite celles que tu utilises par leur identifiant) :\n{conn}\n\n"
            "Réponds par un bloc ```json {\"etiquette\": \"…\", \"confiance\": 0.0, \"connaissances_utilisees\": [], \"indice\": \"…\"} ```.")


def executer(contexte: dict):
    travail = Path(contexte["dossier_travail"])
    budget_ctx = contexte["budget"]
    config = m3.Config(dossier=travail, a_blanc=False, graine=20261024, max_appels=int(budget_ctx["appels_max"]),
                       max_jetons_sortie=10 ** 9, nom_run=f"g{contexte['generation']:03d}", parallelisme=4)
    config.dossier_run.mkdir(parents=True, exist_ok=True)
    journal = m3.Journal(config.journal)
    budget = m3.Budget(config.max_appels, config.max_jetons_sortie)
    client = ClientNoyau(config, journal, budget)
    substrat = m3.charger_substrat(ICI / "SUBSTRAT_BRUT_CONNAISSANCES_INTER_GENERATIONS.json")
    store = m3.magasin(substrat)
    store.setdefault("connaissances", [])
    reponses, arret = [], ""
    exemples = [t for t in contexte["taches_entrainement"]]
    pos = {t["famille"]: t["etiquettes"][0] for t in exemples}
    tableau = m3.Tableau()
    try:
        # ---- M3 : castes sur le tableau (mission + exemples d'entraînement avec vérité) ----
        n_castes = max(2, min(6, (config.max_appels - len(contexte["taches_test"]) - 4) // 2))
        castes = m3.selectionner_castes(m3.castes_du_substrat(substrat), n_castes)
        ex_txt = "\n".join(f"- [{t['id']}] ({t['famille']}, vérité : {t['verite']}) {t['texte']}" for t in exemples[:12])

        def invite(caste, ctx_tableau):
            return (f"MISSION :\n{contexte['mission']}\n\nEXEMPLES D'ENTRAÎNEMENT :\n{ex_txt}\n\n{ctx_tableau}\n\n"
                    "Publie sur le tableau : quels indices distinguent les exemples positifs de chaque famille, et quelles "
                    "formalisations ($$…$$) permettraient de les mesurer. Dis ce qui est conjecture.")

        reponses += m3.executer_vague(client, tableau, castes, invite, "DECOUVERTE", journal, taille_lot=6)
        spectre = m3.analyse_spectrale([p["content"] for p in tableau.posts])
        # ---- M2 : sondes d'écart ----
        reponses += m3.sondes_orthogonales(client, tableau, 1, "DECOUVERTE", "Explore une direction d'indice encore absente du tableau.",
                                           journal, spectre.get("structures_saturees", []))
        # ---- M1 : extraction par l'arbitre ----
        ext = m3.extraire_json_structure(client, f"Tableau de l'essaim :\n{tableau.contexte(20, 12)}",
                                         ["indices_distinctifs"], "DECOUVERTE")
        for e in ext["donnees"]["indices_distinctifs"]:
            if e and e not in [c["enonce"] for c in store["connaissances"]]:
                store["connaissances"].append({"id": f"C-{len(store['connaissances']) + 1:04d}", "enonce": e,
                                               "statut": "non-verifie", "generation": contexte["generation"]})
        # ---- M0 : réponses aux tâches de test ----
        sortie = {}
        for i, t in enumerate(contexte["taches_test"]):
            if budget.appels >= config.max_appels:
                break
            rep = client.appeler(config.arbitre if i % 2 else "GEMINI_ARGON", prompt_tache(t, store["connaissances"]), 0.2, f"TACHE_{t['id']}")
            reponses.append(rep)
            d = m3._charger_json_tolerant(rep.texte.split("```json", 1)[1].split("```", 1)[0]) if rep.ok and "```json" in rep.texte else None
            if isinstance(d, dict) and str(d.get("etiquette", "")).strip().lower() in t["etiquettes"]:
                sortie[t["id"]] = {"etiquette": str(d["etiquette"]).strip().lower(), "confiance": float(d.get("confiance", 0.5) or 0.5)}
        (travail / "reponses_test.json").write_text(json.dumps(sortie, ensure_ascii=False), encoding="utf-8")
        (travail / "metrique_proposee.json").write_text(json.dumps({
            "nom": "capacite_shannon_gram", "definition": "somme de log2(1 + λ) sur les valeurs propres de la matrice de Gram "
            "des vecteurs tf-idf du tableau (nom repris des scripts d'origine ; indice descriptif de diversité)",
            "valeur": spectre.get("capacite_shannon_gram"), "justification": "métrique native de l'essaim de Gemini"},
            ensure_ascii=False), encoding="utf-8")
    except m3.BudgetDepasse as exc:
        arret = f"arrêt sur plafond : {exc}"
        journal.dire("!!! " + arret)
        if not (travail / "reponses_test.json").exists():
            (travail / "reponses_test.json").write_text("{}", encoding="utf-8")
    finally:
        store.setdefault("historique_generations", []).append({"generation": contexte["generation"], "historique": contexte["historique"],
                                                              "appels": budget.etat(), "arret": arret})
        m3.sauver_substrat(ICI / "SUBSTRAT_BRUT_CONNAISSANCES_INTER_GENERATIONS.json", substrat)
        m3.resume_final(config, budget, reponses, {"arret": arret})
        succ = travail / "successeur" / "organisme"
        shutil.copytree(ICI, succ, ignore=shutil.ignore_patterns("__pycache__", "*.secours.json", "runs_debogage"))
    return f"{len(reponses)} appels ; {len(store['connaissances'])} connaissances ; {arret or 'ok'}"
