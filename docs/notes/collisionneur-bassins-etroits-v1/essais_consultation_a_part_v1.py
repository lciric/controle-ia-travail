#!/usr/bin/env python3
"""Essais hors réseau (R5) de consultation_a_part_v1.py : cas sain et artefacts, avec des appelants factices.

Usage : python essais_consultation_a_part_v1.py SCRIPT_COLLISIONNEUR FAITS QUESTION DOSSIER_TEMPORAIRE_NEUF
Aucun appel réseau : chaque fonction d'appel est remplacée par un factice ; les variables de clé ne sont pas lues.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import consultation_a_part_v1 as c  # noqa: E402

SCRIPT, FAITS, QUESTION, TMP = sys.argv[1:5]
TMP = Path(TMP)
TMP.mkdir(parents=True, exist_ok=False)
s = c.charger_script(SCRIPT)
R = s.Reponse
resultats = []


def essai(nom, ok):
    resultats.append((nom, bool(ok)))
    print(f"{'OK ' if ok else 'ÉCHEC'} {nom}")


def factice(reponse, appels):
    def f(modele, prompt, max_tokens):
        appels.append((modele, max_tokens, len(prompt)))
        return reponse(modele) if callable(reponse) else reponse
    return f


base = ["--script", SCRIPT, "--faits", FAITS, "--question", QUESTION]

# 1. Cas sain : trois réponses complètes, marqueur présent, modèle servi conforme.
appels = []
sains = {"argon": factice(lambda m: R(texte="Réponse.\nFIN-DE-CONSULTATION\n", modele_servi=m, fin="STOP",
                                      usage={"entree": 4000, "sortie": 9000}), appels),
         "astra": factice(lambda m: R(texte="Réponse.\nFIN-DE-CONSULTATION", modele_servi=m + "-2026-11-01", fin="stop",
                                      usage={"entree": 4000, "sortie": 7000}), appels),
         "kimi": factice(lambda m: R(texte="Réponse.\nFIN-DE-CONSULTATION", modele_servi=m, fin="stop",
                                     usage={"entree": 4000, "sortie": 20000}), appels)}
code = c.principal(base + ["--sortie", str(TMP / "sain"), "--plafond-usd", "15"], appelants=sains)
essai("sain : code 0", code == 0)
essai("sain : un appel par modèle, plafonds 24000/16000/32000",
      [(a[0], a[1]) for a in appels] == [("gemini-4-argon", 24000), ("gpt-6-astra", 16000), ("kimi-k3.1-pro", 32000)])
rel = {n: json.loads((TMP / "sain" / n / "releve.json").read_text()) for n in ("argon", "astra", "kimi")}
essai("sain : trois consultations valides", all(r["valide"] and r["statut"] == "OK" for r in rel.values()))
essai("sain : coût au barème du script (argon 4000×10 + 9000×50 par million = 0,49)",
      abs(rel["argon"]["cout_usd_bareme_script"] - 0.49) < 1e-9)
essai("sain : prompt, réponse brute, texte écrits",
      all((TMP / "sain" / n / f).exists() for n in rel for f in ("prompt.txt", "reponse-brute.json", "texte.md")))
p = (TMP / "sain" / "argon" / "prompt.txt").read_text(encoding="utf-8")
entete = p.split("<<<DÉBUT FAITS")[0]  # les faits nomment les proposeurs de l'organisme, comme au collisionneur
essai("sain : prompt identique pour les trois ; le modèle consulté n'est pas nommé dans l'en-tête",
      all((TMP / "sain" / n / "prompt.txt").read_text(encoding="utf-8") == p for n in rel)
      and not any(x in entete for x in ("Argon", "Astra", "Kimi", "gemini", "gpt-6", "kimi-k3")))
essai("sain : blocs FAITS et QUESTION aux empreintes des fichiers",
      f"sha256={rel['argon']['sha256_faits']}>>>" in p and f"sha256={rel['argon']['sha256_question']}>>>" in p)
essai("sain : résumé écrit", (TMP / "sain" / "resume.json").exists())

# 2. Artefacts : refus d'Argon (blocage), réponse vide d'Astra, échec de transport de Kimi ; un seul essai chacun.
appels = []
artefacts = {"argon": factice(lambda m: R(fin="BLOCAGE_PROMPT", categorie="OTHER", modele_servi=m,
                                          usage={"entree": 4000, "sortie": 0}), appels),
             "astra": factice(lambda m: R(texte="", modele_servi=m, fin="stop", usage={"entree": 4000, "sortie": 10}),
                              appels),
             "kimi": factice(R(echec="HTTP 429 : compte suspendu"), appels)}
code = c.principal(base + ["--sortie", str(TMP / "artefact"), "--plafond-usd", "15"], appelants=artefacts)
rel = {n: json.loads((TMP / "artefact" / n / "releve.json").read_text()) for n in ("argon", "astra", "kimi")}
essai("artefact : code 0, chaque relevé écrit", code == 0)
essai("artefact : un seul essai par modèle (aucune relance)", len(appels) == 3)
essai("artefact : statuts REFUS / VIDE / ECHEC", (rel["argon"]["statut"], rel["astra"]["statut"], rel["kimi"]["statut"])
      == ("REFUS", "VIDE", "ECHEC"))
essai("artefact : aucune consultation valide", not any(r["valide"] for r in rel.values()))

# 3. Troncature, marqueur absent, modèle différent.
appels = []
autres = {"argon": factice(lambda m: R(texte="début coupé", modele_servi=m, fin="MAX_TOKENS",
                                       usage={"entree": 4000, "sortie": 24000}), appels),
          "astra": factice(lambda m: R(texte="sans marqueur", modele_servi=m, fin="stop",
                                       usage={"entree": 4000, "sortie": 100}), appels),
          "kimi": factice(lambda m: R(texte="x\nFIN-DE-CONSULTATION", modele_servi="kimi-k2", fin="stop",
                                      usage={"entree": 4000, "sortie": 100}), appels)}
code = c.principal(base + ["--sortie", str(TMP / "autres"), "--plafond-usd", "15"], appelants=autres)
rel = {n: json.loads((TMP / "autres" / n / "releve.json").read_text()) for n in ("argon", "astra", "kimi")}
essai("tronqué : TRONQUE, non valide", rel["argon"]["statut"] == "TRONQUE" and not rel["argon"]["valide"])
essai("marqueur absent : OK mais non valide", rel["astra"]["statut"] == "OK" and not rel["astra"]["valide"])
essai("modèle différent : MODELE_DIFFERENT, non valide",
      rel["kimi"]["statut"] == "MODELE_DIFFERENT" and not rel["kimi"]["valide"])

# 4. Plafond : pire cas au-dessus → code 2, aucun appel, aucun dossier.
appels = []
code = c.principal(base + ["--sortie", str(TMP / "plafond"), "--plafond-usd", "1"], appelants=sains)
essai("plafond : code 2, aucun appel, aucun dossier", code == 2 and appels == [] and not (TMP / "plafond").exists())

# 5. Jamais d'écrasement : dossier de sortie existant → code 1, aucun appel.
appels = []
avant = (TMP / "sain" / "argon" / "texte.md").read_bytes()
code = c.principal(base + ["--sortie", str(TMP / "sain"), "--plafond-usd", "15"], appelants=sains)
essai("écrasement : code 1, aucun appel, fichiers intacts",
      code == 1 and appels == [] and (TMP / "sain" / "argon" / "texte.md").read_bytes() == avant)

# 6. Script du collisionneur altéré → code 1.
copie = TMP / "script-altere.py"
copie.write_bytes(Path(SCRIPT).read_bytes() + b"\n# altere\n")
code = c.principal(["--script", str(copie), "--faits", FAITS, "--question", QUESTION, "--plafond-usd", "15",
                    "--devis"])
essai("script altéré : code 1", code == 1)

# 7. Devis : aucun appel, rien d'écrit.
code = c.principal(base + ["--plafond-usd", "15", "--devis"], appelants=sains)
essai("devis : code 0", code == 0)

n_ok = sum(ok for _, ok in resultats)
print(f"{n_ok} sur {len(resultats)} essais réussis")
sys.exit(0 if n_ok == len(resultats) else 1)
