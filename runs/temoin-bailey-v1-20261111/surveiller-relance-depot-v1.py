#!/usr/bin/env python3
"""Contrôle de la relance du témoin de Bailey par le seul dépôt — v1 (session `session_016QhUru4b3VRneQpP2Vn2UX`).

Pour une session sans clé Vast ni Hetzner : récupère la branche de travail (refspec explicite), avance la copie locale
sans fusion, puis lit ce que le poste Hetzner v12 pousse toutes les 10 minutes. Aucune note n'est lue : ni
`notes-v3.jsonl`, ni `technique-v3.jsonl`, ni aucun fichier d'un dossier d'exécution transféré (noms seuls). Les
nouvelles lignes du journal de conduite sont imprimées sans les clés dont le nom évoque une valeur, une note, un rappel
ou un seuil, et les durées par tour réduites à leur nombre, moyenne et maximum.

Rend 0 sans alerte, 2 avec alerte (battement de plus de 30 min, ligne nouvelle au journal, marqueur de fin, transfert),
1 sur erreur de lecture.

Usage : python3 surveiller-relance-depot-v1.py [--depot CHEMIN] [--sans-recuperation]
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path

BRANCHE = "claude/compassionate-meitner-d4ryyk"
REFSPEC = f"+refs/heads/{BRANCHE}:refs/remotes/origin/{BRANCHE}"
BASE = "runs/temoin-bailey-v1-20261111"
SORTIE = f"{BASE}/sortie-conduite-v13"
LIGNES_CONNUES = 13  # journal de conduite au lancement de `principal-relance` (13 novembre, 10:05:32Z)
B, MARGE = 75.0, 2.0
MUET_S = 30 * 60
INTERDITS = ("valeur", "note", "rappel", "seuil", "r_att", "notes-v3", "technique-v3")
MARQUEURS = (f"{BASE}/poste-fini-v12.json", f"{BASE}/bilan-lancement-v13.json", f"{SORTIE}/bilan-conduite-v5.json",
             f"{SORTIE}/rapatriement-v11.json")
CHAMPS_BILAN = ("detruite", "transfert_complet", "arret", "alerte", "cause", "fini", "pid")


def git(depot: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(depot), *args], check=True, capture_output=True, text=True,
                          timeout=600).stdout.strip()


def filtrer(objet):
    """Retire récursivement toute clé interdite ; réduit `durees` à un résumé."""
    if isinstance(objet, dict):
        sortie = {}
        for k, v in objet.items():
            if any(m in str(k).lower() for m in INTERDITS) or str(k) == "J":
                sortie[k] = "(retiré)"
            elif k == "durees" and isinstance(v, dict):
                d = [float(x) for x in v.values() if isinstance(x, (int, float))]
                sortie[k] = {"nombre": len(d), "moyenne_s": round(sum(d) / len(d), 1) if d else None,
                             "max_s": round(max(d), 1) if d else None}
            else:
                sortie[k] = filtrer(v)
        return sortie
    if isinstance(objet, list):
        return [filtrer(x) for x in objet]
    return objet


def heure(t: float) -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(t))


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--depot", default=str(Path(__file__).resolve().parents[2]))
    p.add_argument("--sans-recuperation", action="store_true")
    a = p.parse_args()
    depot = Path(a.depot)
    alertes: list[str] = []
    maintenant = time.time()
    print(f"contrôle à {heure(maintenant)}")
    if not a.sans_recuperation:
        try:
            git(depot, "fetch", "-q", "origin", REFSPEC)
            git(depot, "merge", "-q", "--ff-only", f"origin/{BRANCHE}")
        except subprocess.CalledProcessError as err:
            print(f"récupération ou avance en échec : {err.stderr.strip()[:300]}")
            alertes.append("dépôt non avancé")
    print("tête :", git(depot, "log", "-1", "--format=%h %cI %s"))
    dernier_poste = git(depot, "log", "-1", "--format=%ct %cI", "--grep=poste Hetzner", f"origin/{BRANCHE}")
    if dernier_poste:
        t_poste, iso = dernier_poste.split(" ", 1)
        age = (maintenant - float(t_poste)) / 60
        print(f"dernière poussée du poste : {iso} (il y a {age:.0f} min)")
        if age * 60 > MUET_S:
            alertes.append(f"poste muet depuis {age:.0f} min")
    batt = depot / SORTIE / "arrets-v5.jsonl.battement"
    try:
        b = json.loads(batt.read_text())
        age_b = (maintenant - float(b["t"])) / 60
        print(f"battement du veilleur : {heure(float(b['t']))} (PID {b.get('pid')}, il y a {age_b:.0f} min)")
        if age_b * 60 > MUET_S:
            alertes.append(f"battement vieux de {age_b:.0f} min")
    except (OSError, ValueError, KeyError) as err:
        print(f"battement illisible : {err}")
        alertes.append("battement illisible")
    journal = depot / SORTIE / "conduite-v5.jsonl"
    lignes = journal.read_text(encoding="utf-8").splitlines()
    print(f"journal de conduite : {len(lignes)} lignes")
    for n, ligne in enumerate(lignes[LIGNES_CONNUES:], start=LIGNES_CONNUES + 1):
        try:
            o = json.loads(ligne)
            if isinstance(o.get("t"), (int, float)):
                o["t"] = heure(o["t"])
            print(f"  ligne {n} : {json.dumps(filtrer(o), ensure_ascii=False, sort_keys=True)}")
        except ValueError:
            print(f"  ligne {n} : illisible ({len(ligne)} caractères)")
    if len(lignes) > LIGNES_CONNUES:
        alertes.append(f"{len(lignes) - LIGNES_CONNUES} ligne(s) nouvelle(s) au journal de conduite")
    for m in MARQUEURS:
        f = depot / m
        if f.exists():
            try:
                o = json.loads(f.read_text(encoding="utf-8"))
                vus = {k: o[k] for k in CHAMPS_BILAN if isinstance(o, dict) and k in o}
            except ValueError:
                vus = "(illisible)"
            print(f"marqueur présent : {m} {json.dumps(vus, ensure_ascii=False, default=str)}")
            alertes.append(f"marqueur {Path(m).name}")
    noms = sorted(x.name + ("/" if x.is_dir() else "") for x in (depot / SORTIE).iterdir())
    attendus = {"amorce-v5.sh", "archive/", "arrets-v5.jsonl.battement", "arrets-v5.jsonl.err", "conduite-v5.jsonl",
                "manifeste-v3-mise-en-place.json", "manifeste-v3-mise-en-place.json.sha256", "manifeste-v3-relance.json",
                "manifeste-v3-relance.json.sha256", "manifeste-v3.json", "manifeste-v3.json.sha256", "poste-v5.json"}
    nouveaux = [x for x in noms if x not in attendus]
    if nouveaux:
        print("noms nouveaux dans la sortie v13 :", ", ".join(nouveaux))
        alertes.append("noms nouveaux dans la sortie v13")
    err = depot / SORTIE / "arrets-v5.jsonl.err"
    if err.exists() and err.stat().st_size:
        print(f"arrets-v5.jsonl.err non vide ({err.stat().st_size} octets)")
        alertes.append("erreur du veilleur")
    poste = json.loads((depot / SORTIE / "poste-v5.json").read_text())
    d = sum(float(i["c"]) * ((i["destruction"] or maintenant) - float(i["creation"])) / 3600 for i in poste["instances"])
    ouvertes = [i for i in poste["instances"] if not i["destruction"]]
    taux = sum(float(i["c"]) for i in ouvertes)
    reste_h = (B - MARGE - d) / taux if taux else float("inf")
    print(f"D (calcul du poste, taux × durée) : {d:.2f} USD ; instances ouvertes : {[i['id'] for i in ouvertes]}"
          + (f" ; B − 2 dans {reste_h:.1f} h, vers {heure(maintenant + reste_h * 3600)}" if taux else ""))
    print("ALERTES : " + ("; ".join(alertes) if alertes else "aucune"))
    return 2 if alertes else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as err:  # lecture impossible : rapporté, jamais masqué
        print(f"ERREUR {type(err).__name__} : {err}")
        sys.exit(1)
