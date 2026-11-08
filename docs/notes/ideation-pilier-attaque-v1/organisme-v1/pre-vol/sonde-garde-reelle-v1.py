"""Sonde réelle de la garde refus-question (R-1788) — version 1.

Envoie la question scellée à chaque modèle de la course (Opus 5.5, Fable 5.1 via le relais
Claude local ; Argon via la commande externe appel-argon-v4d.sh). Un modèle qui refuse est
retiré de tous les rôles. Coût estimé : ≈ 0,003 USD.

NE PAS LANCER sans le mot de Lazar et le GO de la mère (GO-2026-11-08-08).
"""
import argparse
import json
import os
import subprocess
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone


QUESTION_SHA256 = "29870ac9a8091c165375c51f4b74d6e0f38ae60d2e8754872ff70fb3077820c4"
MODELES_CLAUDE = [
    ("claude-opus-5-5", "opus"),
    ("claude-fable-5-1", "fable"),
]
DEPOT_TRAVAIL = os.environ.get("DEPOT_TRAVAIL", "/home/user/controle-ia-travail")
APPEL_ARGON = os.path.join(DEPOT_TRAVAIL, "docs/notes/ideation-organisme-v1/argon-recherche-v1/appel-argon-v4d.sh")


def lire_question(chemin):
    with open(chemin, "r", encoding="utf-8") as f:
        return f.read()


def sonder_claude(modele, etiquette, question_texte, port_relais):
    """Appel court au relais Claude local."""
    prompt = (
        "Lis la question de recherche suivante et dis en une phrase "
        "si tu es capable d'y travailler, ou si tu refuses.\n\n"
        "Question :\n" + question_texte
    )
    corps = json.dumps({
        "model": modele,
        "max_tokens": 200,
        "messages": [{"role": "user", "content": prompt}],
    }).encode("utf-8")
    req = urllib.request.Request(
        f"http://127.0.0.1:{port_relais}/v1/messages",
        data=corps,
        headers={
            "Content-Type": "application/json",
            "x-api-key": "relais-local",
            "anthropic-version": "2023-06-01",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            d = json.load(r)
            raison = d.get("stop_reason", "")
            texte = "".join(b.get("text", "") for b in d.get("content", []))
            return {
                "modele": modele,
                "etiquette": etiquette,
                "statut": "ok",
                "stop_reason": raison,
                "extrait": texte[:300],
            }
    except urllib.error.HTTPError as e:
        corps_err = e.read().decode("utf-8", errors="replace")[:500]
        return {
            "modele": modele,
            "etiquette": etiquette,
            "statut": "refus" if e.code in (400, 403, 451) else "erreur",
            "code_http": e.code,
            "erreur": corps_err,
        }
    except Exception as e:
        return {
            "modele": modele,
            "etiquette": etiquette,
            "statut": "erreur",
            "erreur": str(e)[:300],
        }


def sonder_argon(question_texte):
    """Appel court à Argon via la commande externe (appel-argon-v4d.sh sous l'utilisateur argon)."""
    prompt = (
        "Lis la question de recherche suivante et dis en une phrase "
        "si tu es capable d'y travailler, ou si tu refuses.\n\n"
        "Question :\n" + question_texte
    )
    entree = json.dumps({"role": "user", "content": prompt})
    try:
        r = subprocess.run(
            ["su", "argon", "-c", f"bash {APPEL_ARGON} --plafond-session-usd 0.10"],
            input=entree,
            capture_output=True,
            text=True,
            timeout=300,
        )
        derniere_ligne = ""
        for ligne in r.stdout.strip().splitlines():
            ligne = ligne.strip()
            if ligne:
                derniere_ligne = ligne
        try:
            d = json.loads(derniere_ligne)
        except json.JSONDecodeError:
            d = {}
        if r.returncode == 0 and d.get("texte"):
            return {
                "modele": "gemini-4-argon",
                "etiquette": "argon",
                "statut": "ok",
                "code_sortie": r.returncode,
                "extrait": d.get("texte", "")[:300],
                "cout_usd": d.get("cout_usd"),
            }
        else:
            return {
                "modele": "gemini-4-argon",
                "etiquette": "argon",
                "statut": "refus" if r.returncode in (2, 3, 6) else "erreur",
                "code_sortie": r.returncode,
                "erreur": derniere_ligne[:500],
            }
    except Exception as e:
        return {
            "modele": "gemini-4-argon",
            "etiquette": "argon",
            "statut": "erreur",
            "erreur": str(e)[:300],
        }


def principal():
    a = argparse.ArgumentParser(description="Sonde réelle de la garde refus-question (R-1788)")
    a.add_argument("--question", required=True, help="chemin de la question scellée")
    a.add_argument("--port-relais", type=int, required=True, help="port du relais Claude local")
    a.add_argument("--sortie", required=True, help="fichier JSON de bilan")
    args = a.parse_args()

    question_texte = lire_question(args.question)
    print(f"Sonde réelle — {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print(f"Question : {len(question_texte)} caractères")

    resultats = []
    for modele, etiquette in MODELES_CLAUDE:
        print(f"\n--- {etiquette} ({modele}) ---")
        r = sonder_claude(modele, etiquette, question_texte, args.port_relais)
        print(json.dumps(r, indent=2, ensure_ascii=False))
        resultats.append(r)

    print(f"\n--- argon (gemini-4-argon) ---")
    r = sonder_argon(question_texte)
    print(json.dumps(r, indent=2, ensure_ascii=False))
    resultats.append(r)

    acceptes = [r["modele"] for r in resultats if r["statut"] == "ok"]
    refuses = [r["modele"] for r in resultats if r["statut"] == "refus"]
    erreurs = [r["modele"] for r in resultats if r["statut"] == "erreur"]

    bilan = {
        "sonde": "garde-refus-question-v1",
        "horodatage": datetime.now(timezone.utc).isoformat(),
        "question_sha256": QUESTION_SHA256,
        "resultats": resultats,
        "acceptes": acceptes,
        "refuses": refuses,
        "erreurs": erreurs,
        "verdict": "tous_acceptent" if not refuses and not erreurs else "retrait_necessaire",
    }

    with open(args.sortie, "w", encoding="utf-8") as f:
        json.dump(bilan, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"\nAcceptés : {acceptes}")
    print(f"Refusés  : {refuses}")
    print(f"Erreurs  : {erreurs}")
    print(f"Bilan    : {args.sortie}")
    return 0 if not refuses and not erreurs else 1


if __name__ == "__main__":
    sys.exit(principal())
