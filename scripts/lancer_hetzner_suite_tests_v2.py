"""Lanceur v2 : crée un serveur Hetzner jetable qui joue une fois la suite complète des tests du dépôt.

Remplace la v1 (gardée intacte, R12) selon la contre-lecture de classe B du lot v1 : échéance du GO réellement
contrôlée (clé « echeance » de la garde), création protégée contre le serveur orphelin, garde-fous sur les entrées,
plafond de dépense vérifié contre le GO, filet indépendant dans les données de démarrage.
GO de type calcul exigé (registres/go.md), ligne d'engagement préalable au registre des dépenses, zéro serveur actif,
prix relu par l'API. Jetons jamais écrits sur la sortie ; mot de passe racine renvoyé par l'API jamais lu.

Usage : GO_ID=GO-2026-11-28-04 python scripts/lancer_hetzner_suite_tests_v2.py --commit <sha> --run-id <id> ...
"""
from __future__ import annotations

import argparse
import base64
import gzip
import importlib.util
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
API = os.environ.get("HCLOUD_API", "https://api.hetzner.cloud/v1")
AMORCE = RACINE / "scripts" / "amorce_hetzner_suite_tests_v2.sh"
FILET = RACINE / "scripts" / "filet_hetzner_suite_tests_v2.sh"
DEPOT_URL = "https://github.com/lciric/controle-ia-travail.git"   # jamais lciric/controle-ia (copie publique)
TYPES = ("cx53", "cpx51", "ccx33", "cpx41")
LIEUX = ("fsn1", "nbg1", "hel1")
LIMITE_DONNEES_DEMARRAGE = 32 * 1024
PLAFOND_SECONDES_MAX = 8 * 3600
MARGE_FILET = 2700                       # le filet indépendant agit 45 min après le plafond interne
TAUX_USD_EUR = 1.25                      # taux du registre des dépenses
NOM = re.compile(r"^[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?$")
BRANCHE = re.compile(r"^[A-Za-z0-9._/-]+$")


def appel(methode: str, chemin: str, corps: dict | None = None) -> tuple[int, dict]:
    jeton = os.environ["HCLOUD_TOKEN"]
    req = urllib.request.Request(API + chemin, method=methode,
                                 data=None if corps is None else json.dumps(corps).encode(),
                                 headers={"Authorization": f"Bearer {jeton}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, json.loads(r.read() or b"{}")
    except urllib.error.HTTPError as e:
        try:
            return e.code, json.loads(e.read() or b"{}")
        except json.JSONDecodeError:
            return e.code, {}


def exiger_go(go_id: str, registre: Path, aujourd_hui: date) -> float:
    """Type calcul, accordé par Lazar, dans sa période de validité, non révoqué ; rend le plafond en USD."""
    spec = importlib.util.spec_from_file_location("garde", RACINE / ".claude" / "hooks" / "garde_calcul.py")
    garde = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(garde)
    lignes = garde.lire_go(registre)
    g = lignes.get(go_id)
    if not g or g.get("type") != "calcul":
        sys.exit(f"ARRÊT : {go_id} absent du registre ou d'un autre type que « calcul »")
    if g.get("par") != "Lazar":
        sys.exit(f"ARRÊT : {go_id} n'est pas accordé par Lazar")
    ech = g.get("echeance")
    if ech is None or not (g["accorde"] <= aujourd_hui <= ech):
        sys.exit(f"ARRÊT : {go_id} hors de sa période de validité ({g['accorde']} → {ech})")
    if any(r["type"] == "révocation" and (go_id in r["perimetre"] or go_id in r["ref"]) for r in lignes.values()):
        sys.exit(f"ARRÊT : {go_id} révoqué")
    for ligne in registre.read_text(encoding="utf-8").splitlines():
        if ligne.startswith(f"| {go_id} |"):
            cellules = [c.strip() for c in ligne.strip().strip("|").split("|")]
            m = re.match(r"^(\d+(?:[.,]\d+)?)\s*USD", cellules[4])
            if m:
                return float(m.group(1).replace(",", "."))
    sys.exit(f"ARRÊT : plafond en USD illisible pour {go_id}")


def exiger_engagement(go_id: str, run_id: str, registre: Path) -> None:
    texte = registre.read_text(encoding="utf-8")
    if not any(go_id in l and run_id in l and "engagement" in l.lower() for l in texte.splitlines()):
        sys.exit(f"ARRÊT : aucune ligne d'engagement {go_id} / {run_id} au registre des dépenses")


def exiger_entrees(a: argparse.Namespace) -> None:
    if a.depot_url != DEPOT_URL:
        sys.exit(f"ARRÊT : dépôt {a.depot_url} refusé (seul {DEPOT_URL} est admis)")
    if not NOM.match(a.run_id):
        sys.exit("ARRÊT : identifiant de course invalide (nom de serveur : minuscules, chiffres, tirets, 63 au plus)")
    for b in (a.branche_code, a.branche_sortie):
        if not BRANCHE.match(b):
            sys.exit(f"ARRÊT : nom de branche invalide : {b}")
    if not re.fullmatch(r"[0-9a-f]{40}", a.commit):
        sys.exit("ARRÊT : commit attendu en 40 caractères hexadécimaux")
    if not (600 <= a.plafond_secondes <= PLAFOND_SECONDES_MAX):
        sys.exit(f"ARRÊT : plafond de {a.plafond_secondes} s hors de [600, {PLAFOND_SECONDES_MAX}]")


def branche_existe(branche: str) -> bool:
    r = subprocess.run(["git", "-C", str(RACINE), "ls-remote", "origin", f"refs/heads/{branche}"],
                       capture_output=True, text=True, timeout=60)
    if r.returncode != 0:
        sys.exit("ARRÊT : git ls-remote illisible ; impossible de prouver que la branche de sortie est neuve")
    return bool(r.stdout.strip())


def b64gz(chemin: Path) -> str:
    return base64.b64encode(gzip.compress(chemin.read_bytes(), mtime=0)).decode()


def donnees_demarrage(a: argparse.Namespace) -> str:
    gh = os.environ[a.variable_jeton_github].strip()
    hc = os.environ["HCLOUD_TOKEN"].strip()
    for nom, valeur in (("gh", gh), ("hc", hc)):
        if not valeur or any(c in valeur for c in "'\n\r \\"):
            sys.exit(f"ARRÊT : jeton {nom} vide ou de forme inattendue")
    contraintes = Path(a.contraintes).read_text(encoding="utf-8")
    parametres = "\n".join([
        f"RUN_ID={a.run_id}", f"DEPOT_URL={a.depot_url}", f"COMMIT_CODE={a.commit}",
        f"BRANCHE_CODE={a.branche_code}", f"BRANCHE_SORTIE={a.branche_sortie}",
        f"PLAFOND_SECONDES={a.plafond_secondes}", "TRAVAIL=/opt/suite-tests",
        "GH_TOKEN_FILE=/opt/suite-tests/jeton-github", "HC_TOKEN_FILE=/opt/suite-tests/jeton-hcloud",
        "CONTRAINTES=/opt/suite-tests/contraintes-v2.txt", "UTILISATEUR=essais",
        "DEPOT=/home/user/controle-ia-travail",
    ])
    return "\n".join([
        "#!/bin/bash",
        "set -u",
        "umask 077",
        "systemctl disable --now ssh.socket ssh.service >/dev/null 2>&1 || true",
        "mkdir -p /opt/suite-tests",
        f"printf '%s\\n' '{gh}' > /opt/suite-tests/jeton-github",
        f"printf '%s\\n' '{hc}' > /opt/suite-tests/jeton-hcloud",
        f"printf 'Authorization: Bearer %s\\n' '{hc}' > /opt/suite-tests/entete-filet",
        "cat > /opt/suite-tests/contraintes-v2.txt <<'FIN_CONTRAINTES'",
        contraintes.rstrip("\n"),
        "FIN_CONTRAINTES",
        "cat > /opt/suite-tests/parametres.env <<'FIN_PARAMETRES'",
        parametres,
        "FIN_PARAMETRES",
        f"echo '{b64gz(FILET)}' | base64 -d | gunzip > /opt/suite-tests/filet.sh",
        f"systemd-run --unit=suite-tests-filet --on-active={a.plafond_secondes + MARGE_FILET}s "
        "/bin/bash /opt/suite-tests/filet.sh /opt/suite-tests/entete-filet /opt/suite-tests/journal-filet.txt",
        f"echo '{b64gz(AMORCE)}' | base64 -d | gunzip > /opt/suite-tests/amorce.sh",
        "systemd-run --unit=suite-tests --collect /bin/bash /opt/suite-tests/amorce.sh /opt/suite-tests/parametres.env",
        "",
    ])


def serveur_de_la_course(run_id: str) -> dict | None:
    code, d = appel("GET", f"/servers?label_selector=run%3D{run_id}")
    s = d.get("servers", []) if code == 200 else []
    return s[0] if len(s) == 1 else None


def ecrire_etat(a, go_id, s, type_, lieu, prix) -> None:
    etat = {"go": go_id, "run_id": a.run_id, "identifiant": s["id"], "nom": s.get("name"), "type": type_,
            "lieu": lieu, "prix_eur_h_brut": prix, "cree": s.get("created"), "commit": a.commit,
            "branche_sortie": a.branche_sortie, "plafond_secondes": a.plafond_secondes}
    print(json.dumps(etat, ensure_ascii=False), flush=True)      # l'identifiant d'abord sur la sortie
    Path(a.etat).write_text(json.dumps(etat, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--commit", required=True)
    p.add_argument("--run-id", required=True)
    p.add_argument("--branche-code", required=True)
    p.add_argument("--branche-sortie", required=True)
    p.add_argument("--contraintes", required=True)
    p.add_argument("--plafond-secondes", type=int, default=8 * 3600)
    p.add_argument("--depot-url", default=DEPOT_URL)
    p.add_argument("--variable-jeton-github", default="CONTROLE_IA_GITHUB_TOKEN_2")
    p.add_argument("--etat", required=True, help="fichier JSON où écrire l'identifiant du serveur (sans secret)")
    p.add_argument("--essai-sans-creation", action="store_true")
    a = p.parse_args()

    go_id = os.environ.get("GO_ID", "")
    plafond_usd = exiger_go(go_id, RACINE / "registres" / "go.md", date.today())
    exiger_engagement(go_id, a.run_id, RACINE / "registres" / "depenses.md")
    exiger_entrees(a)
    if branche_existe(a.branche_sortie) or branche_existe(a.branche_sortie + "-reduit"):
        sys.exit(f"ARRÊT : la branche de sortie {a.branche_sortie} (ou sa forme réduite) existe déjà")
    code, d = appel("GET", "/servers")
    if code != 200:
        sys.exit(f"ARRÊT : liste des serveurs illisible ({code})")
    if d.get("servers"):
        sys.exit(f"ARRÊT : {len(d['servers'])} serveur(s) déjà actif(s) dans le projet ; vérifier avant création")
    donnees = donnees_demarrage(a)
    if len(donnees.encode()) > LIMITE_DONNEES_DEMARRAGE:
        sys.exit(f"ARRÊT : données de démarrage de {len(donnees.encode())} octets (limite {LIMITE_DONNEES_DEMARRAGE})")
    code, d = appel("GET", "/server_types?per_page=50")
    prix = {(t["name"], q["location"]): float(q["price_hourly"]["gross"])
            for t in d.get("server_types", []) for q in t.get("prices", [])}
    heures_max = (a.plafond_secondes + MARGE_FILET + 3600) / 3600          # filet compris, heure entamée comprise
    admissibles = [(t, l) for t in TYPES for l in LIEUX
                   if (t, l) in prix and prix[(t, l)] * heures_max * TAUX_USD_EUR <= plafond_usd]
    if a.essai_sans_creation:
        print(json.dumps({"essai": True, "octets_donnees_demarrage": len(donnees.encode()), "plafond_usd": plafond_usd,
                          "admissibles": [f"{t}@{l} {prix[(t, l)]} EUR/h" for t, l in admissibles]}, indent=1))
        return 0
    if not admissibles:
        sys.exit("ARRÊT : aucun type de serveur ne tient sous le plafond du GO au pire cas")
    for type_, lieu in admissibles:
        corps = {"name": a.run_id, "server_type": type_, "location": lieu, "image": "ubuntu-24.04",
                 "start_after_create": True, "user_data": donnees,
                 "labels": {"programme": "controle-ia", "run": a.run_id, "go": go_id},
                 "public_net": {"enable_ipv4": True, "enable_ipv6": True}}
        try:
            code, d = appel("POST", "/servers", corps)
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            code, d = -1, {"error": {"code": type(e).__name__, "message": str(e)[:120]}}
        if code == 201:
            ecrire_etat(a, go_id, d["server"], type_, lieu, prix[(type_, lieu)])
            return 0
        s = serveur_de_la_course(a.run_id)       # réponse perdue ou ambiguë : le serveur existe-t-il quand même ?
        if s is not None:
            ecrire_etat(a, go_id, s, type_, lieu, prix[(type_, lieu)])
            print("serveur retrouvé par son étiquette après une réponse ambiguë ; aucun nouvel essai", file=sys.stderr)
            return 0
        err = d.get("error", {})
        print(f"refus {type_}@{lieu} : {code} {err.get('code')} {str(err.get('message', ''))[:120]}", file=sys.stderr)
    sys.exit("ARRÊT : aucun type de serveur accepté")


if __name__ == "__main__":
    sys.exit(main())
