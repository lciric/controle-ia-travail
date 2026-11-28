"""Lanceur v1 : crée un serveur Hetzner jetable qui joue une fois la suite complète des tests du dépôt.

GO de type calcul exigé (registres/go.md, lu par la garde du dépôt), ligne d'engagement préalable au registre des
dépenses (vérifiée ici), zéro serveur actif dans le projet avant création, prix relu par l'API. Les jetons ne sont
jamais écrits sur la sortie : seuls l'identifiant, le type, le lieu et le prix du serveur le sont. Le mot de passe
racine renvoyé par l'API est jeté sans être lu.

Usage : GO_ID=GO-2026-11-28-04 python scripts/lancer_hetzner_suite_tests_v1.py --commit <sha> --run-id <id> ...
"""
from __future__ import annotations

import argparse
import base64
import importlib.util
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
API = os.environ.get("HCLOUD_API", "https://api.hetzner.cloud/v1")
AMORCE = RACINE / "scripts" / "amorce_hetzner_suite_tests_v1.sh"
# ordre de repli : 16 cœurs partagés au plus bas prix, puis 16 partagés, 8 dédiés, 8 partagés
TYPES = ("cx53", "cpx51", "ccx33", "cpx41")
LIEUX = ("fsn1", "nbg1", "hel1")
LIMITE_DONNEES_DEMARRAGE = 32 * 1024


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


def exiger_go(go_id: str) -> None:
    spec = importlib.util.spec_from_file_location("garde", RACINE / ".claude" / "hooks" / "garde_calcul.py")
    garde = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(garde)
    lignes = garde.lire_go(RACINE / "registres" / "go.md")
    ligne = lignes.get(go_id)
    if not ligne or ligne.get("type") != "calcul":
        sys.exit(f"ARRÊT : {go_id} absent de registres/go.md ou d'un autre type que « calcul »")
    if ligne.get("échéance") and ligne["échéance"] < date.today():
        sys.exit(f"ARRÊT : {go_id} échu le {ligne['échéance']}")


def exiger_engagement(go_id: str, run_id: str) -> None:
    texte = (RACINE / "registres" / "depenses.md").read_text(encoding="utf-8")
    if not any(go_id in l and run_id in l and "engagement" in l.lower() for l in texte.splitlines()):
        sys.exit(f"ARRÊT : aucune ligne d'engagement {go_id} / {run_id} au registre des dépenses")


def donnees_demarrage(args: argparse.Namespace) -> str:
    gh = os.environ[args.variable_jeton_github].strip()
    hc = os.environ["HCLOUD_TOKEN"].strip()
    contraintes = Path(args.contraintes).read_text(encoding="utf-8")
    amorce_b64 = base64.b64encode(AMORCE.read_bytes()).decode()
    parametres = "\n".join([
        f"RUN_ID={args.run_id}", f"DEPOT_URL={args.depot_url}", f"COMMIT_CODE={args.commit}",
        f"BRANCHE_CODE={args.branche_code}", f"BRANCHE_SORTIE={args.branche_sortie}",
        f"PLAFOND_SECONDES={args.plafond_secondes}", "TRAVAIL=/opt/suite-tests",
        "GH_TOKEN_FILE=/opt/suite-tests/jeton-github", "HC_TOKEN_FILE=/opt/suite-tests/jeton-hcloud",
        "CONTRAINTES=/opt/suite-tests/contraintes-v1.txt", "UTILISATEUR=essais",
    ])
    for nom, valeur in (("gh", gh), ("hc", hc)):
        if not valeur or any(c in valeur for c in "'\n\r "):
            sys.exit(f"ARRÊT : jeton {nom} vide ou de forme inattendue")
    return "\n".join([
        "#!/bin/bash",
        "set -u",
        "umask 077",
        "systemctl disable --now ssh.socket ssh.service >/dev/null 2>&1 || true",
        "mkdir -p /opt/suite-tests",
        f"printf '%s\\n' '{gh}' > /opt/suite-tests/jeton-github",
        f"printf '%s\\n' '{hc}' > /opt/suite-tests/jeton-hcloud",
        "cat > /opt/suite-tests/contraintes-v1.txt <<'FIN_CONTRAINTES'",
        contraintes.rstrip("\n"),
        "FIN_CONTRAINTES",
        "cat > /opt/suite-tests/parametres.env <<'FIN_PARAMETRES'",
        parametres,
        "FIN_PARAMETRES",
        f"echo '{amorce_b64}' | base64 -d > /opt/suite-tests/amorce.sh",
        "systemd-run --unit=suite-tests --collect /bin/bash /opt/suite-tests/amorce.sh /opt/suite-tests/parametres.env",
        "",
    ])


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--commit", required=True)
    p.add_argument("--run-id", required=True)
    p.add_argument("--branche-code", required=True)
    p.add_argument("--branche-sortie", required=True)
    p.add_argument("--contraintes", required=True)
    p.add_argument("--plafond-secondes", type=int, default=8 * 3600)
    p.add_argument("--depot-url", default=os.environ.get("DEPOT_URL", "https://github.com/lciric/controle-ia-travail.git"))
    p.add_argument("--variable-jeton-github", default="CONTROLE_IA_GITHUB_TOKEN_2")
    p.add_argument("--etat", required=True, help="fichier JSON où écrire l'identifiant du serveur (sans secret)")
    p.add_argument("--essai-sans-creation", action="store_true")
    a = p.parse_args()

    go_id = os.environ.get("GO_ID", "")
    exiger_go(go_id)
    exiger_engagement(go_id, a.run_id)
    if len(a.commit) != 40:
        sys.exit("ARRÊT : commit attendu en 40 caractères")
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
    if a.essai_sans_creation:
        print(json.dumps({"essai": True, "octets_donnees_demarrage": len(donnees.encode()),
                          "prix_eur_h": {f"{t}@{l}": prix.get((t, l)) for t in TYPES for l in LIEUX}}, indent=1))
        return 0
    for type_ in TYPES:
        for lieu in LIEUX:
            if (type_, lieu) not in prix:
                continue
            corps = {"name": a.run_id[:63], "server_type": type_, "location": lieu, "image": "ubuntu-24.04",
                     "start_after_create": True, "user_data": donnees,
                     "labels": {"programme": "controle-ia", "run": a.run_id[:63], "go": go_id},
                     "public_net": {"enable_ipv4": True, "enable_ipv6": True}}
            code, d = appel("POST", "/servers", corps)
            if code == 201:
                s = d["server"]
                etat = {"go": go_id, "run_id": a.run_id, "identifiant": s["id"], "nom": s["name"], "type": type_,
                        "lieu": lieu, "prix_eur_h_brut": prix[(type_, lieu)], "cree": s.get("created"),
                        "commit": a.commit, "branche_sortie": a.branche_sortie,
                        "plafond_secondes": a.plafond_secondes}
                Path(a.etat).write_text(json.dumps(etat, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
                print(json.dumps(etat, ensure_ascii=False))
                return 0
            err = d.get("error", {})
            print(f"refus {type_}@{lieu} : {code} {err.get('code')} {err.get('message', '')[:120]}", file=sys.stderr)
    sys.exit("ARRÊT : aucun type de serveur accepté")


if __name__ == "__main__":
    sys.exit(main())
