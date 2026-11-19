#!/usr/bin/env python3
"""Vérification de la clé Claude « Rigaud » par un seul appel minimal — version 1.

Décision : choix de Lazar GO-2026-11-19-31 (la part Claude de l'essai de mesure des lecteurs du bras A passe par la clé
Rigaud) ; ligne de calcul GO-2026-11-19-32 (un appel minimal, un jeton de sortie, plafond 0,01 USD) ; règle de permission
posée sur le mot de Lazar « go reco a » (session de relance, 2026-11-19), qui n'autorise que la commande exacte :

    GO_ID=GO-2026-11-19-32 python3 -I scripts/verifier_cle_claude_v1.py

Ce que fait le programme, et rien d'autre :
1. exige GO_ID=GO-2026-11-19-32 dans l'environnement, et la ligne GO-2026-11-19-32 au registre des GO de la branche
   principale (lu par `git show origin/main:registres/go.md`), de type « calcul », plafond 0,01 USD ;
2. refuse de partir si un relevé de vérification existe déjà (un seul appel, jamais rejoué) ;
3. lit la clé par son nom (RR_ANTHROPIC_API_KEY_RIGAUD), ne l'écrit ni ne l'affiche jamais ;
4. envoie un seul message minimal au modèle le moins cher (claude-haiku-5-5), max_tokens 1, sans température, sans
   reprise (aucune boucle, une seule requête) ;
5. relève et scelle seulement : heure d'envoi et de retour, code HTTP, type d'erreur s'il y en a, motif de fin, modèle
   servi, compteurs de jetons, coût calculé au tarif public relevé (0,10 et 0,50 USD par million de jetons d'entrée et de
   sortie ; estimation préalable des lectures, section des tarifs) — jamais le texte de la réponse.

Le coût au pire d'un tel appel est de l'ordre de 1e-5 USD, très sous le plafond de 0,01 USD.
"""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

GO_ATTENDU = "GO-2026-11-19-32"
NOM_CLE = "RR_ANTHROPIC_API_KEY_RIGAUD"
MODELE = "claude-haiku-5-5"
PRIX_ENTREE, PRIX_SORTIE = 0.10, 0.50  # USD par million de jetons
PLAFOND_USD = 0.01
RACINE = Path(__file__).resolve().parents[1]
DOSSIER = RACINE / "runs" / "verification-cle-claude-rigaud-v1"
RELEVE = DOSSIER / "releve-verification-v1.json"


def arreter(motif: str) -> None:
    print(f"ARRÊT : {motif}", file=sys.stderr)
    sys.exit(2)


def heure() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def verifier_go() -> str:
    if os.environ.get("GO_ID") != GO_ATTENDU:
        arreter(f"GO_ID absent ou différent de {GO_ATTENDU}")
    try:
        registre = subprocess.run(["git", "-C", str(RACINE), "show", "origin/main:registres/go.md"],
                                  check=True, capture_output=True, text=True).stdout
    except subprocess.CalledProcessError as erreur:
        arreter(f"registre des GO de la branche principale illisible ({erreur.returncode})")
    lignes = [l for l in registre.splitlines() if l.startswith(f"| {GO_ATTENDU} |")]
    if len(lignes) != 1:
        arreter(f"{len(lignes)} ligne(s) {GO_ATTENDU} au registre de la branche principale (une seule attendue)")
    ligne = lignes[0]
    if "| calcul |" not in ligne or "0,01 USD" not in ligne:
        arreter(f"la ligne {GO_ATTENDU} n'est pas une ligne de calcul plafonnée à 0,01 USD")
    return hashlib.sha256(ligne.encode("utf-8")).hexdigest()


def main() -> None:
    empreinte_ligne = verifier_go()
    if RELEVE.exists():
        arreter(f"relevé déjà présent ({RELEVE.relative_to(RACINE)}) : la vérification ne se rejoue pas")
    cle = os.environ.get(NOM_CLE, "")
    if not cle:
        arreter(f"variable {NOM_CLE} absente")
    corps = json.dumps({"model": MODELE, "max_tokens": 1,
                        "messages": [{"role": "user", "content": "ok"}]}).encode("utf-8")
    requete = urllib.request.Request("https://api.anthropic.com/v1/messages", data=corps, method="POST", headers={
        "x-api-key": cle, "anthropic-version": "2023-06-01", "content-type": "application/json"})
    del cle
    DOSSIER.mkdir(parents=True, exist_ok=True)
    releve = {"go": GO_ATTENDU, "empreinte_ligne_go": empreinte_ligne, "modele_demande": MODELE,
              "max_tokens": 1, "heure_envoi": heure()}
    try:
        with urllib.request.urlopen(requete, timeout=60) as reponse:
            code, donnees = reponse.status, json.loads(reponse.read().decode("utf-8"))
    except urllib.error.HTTPError as erreur:
        code = erreur.code
        try:
            donnees = json.loads(erreur.read().decode("utf-8"))
        except (ValueError, UnicodeDecodeError):
            donnees = {}
    except (urllib.error.URLError, TimeoutError) as erreur:
        code, donnees = None, {"erreur_reseau": type(erreur).__name__}
    releve["heure_retour"] = heure()
    releve["code_http"] = code
    if isinstance(donnees.get("error"), dict):
        releve["type_erreur"] = donnees["error"].get("type")
    usage = donnees.get("usage") or {}
    releve["modele_servi"] = donnees.get("model")
    releve["motif_de_fin"] = donnees.get("stop_reason")
    releve["jetons_entree"] = usage.get("input_tokens")
    releve["jetons_sortie"] = usage.get("output_tokens")
    if releve["jetons_entree"] is not None and releve["jetons_sortie"] is not None:
        cout = (releve["jetons_entree"] * PRIX_ENTREE + releve["jetons_sortie"] * PRIX_SORTIE) / 1e6
        releve["cout_calcule_usd"] = round(cout, 8)
        releve["sous_le_plafond"] = cout <= PLAFOND_USD
    if "erreur_reseau" in donnees:
        releve["erreur_reseau"] = donnees["erreur_reseau"]
    RELEVE.write_text(json.dumps(releve, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    empreinte = hashlib.sha256(RELEVE.read_bytes()).hexdigest()
    RELEVE.with_name(RELEVE.name + ".sha256").write_text(f"{empreinte}  {RELEVE.name}\n", encoding="utf-8")
    print(json.dumps(releve, ensure_ascii=False))


if __name__ == "__main__":
    main()
