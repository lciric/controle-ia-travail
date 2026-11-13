#!/usr/bin/env python3
"""Épreuve sans dépense : quel en-tête d'authentification le kit d'agent (claude_agent_sdk et l'outil en ligne de commande
qu'il lance) présente-t-il au relais, selon l'environnement hérité ? — v1.

Écrit par le préparateur (Claude Opus 5.5), 13 novembre 2026, pour le lanceur v3 de l'atelier sur les bassins étroits
(point 1 de la demande de la mère, après l'échec de la génération 1 : 401 « jeton différent du jeton factice »).

**Aucun appel de modèle, aucun réseau** : chaque essai tourne dans `bwrap --unshare-net` (espace réseau neuf : seule la
boucle locale de cet espace existe ; rien ne sort du conteneur), avec un **faux amont** sur 127.0.0.1 de cet espace, qui
répond 401 à tout et note, par requête, le chemin, les **noms** des en-têtes, et seulement si `x-api-key` ou
`Authorization` **égalent** le jeton factice du relais (`relais-local-sans-cle`) ; aucune valeur d'en-tête n'est écrite.
`/tmp` est un tmpfs neuf (la prise de messagerie de la session hôte y est cachée) ; `/root` est soit un tmpfs vide (`home
= vide`, l'environnement seul varie), soit le vrai `/root` en lecture seule (`home = lecture_seule`, comme la session : rien
n'y est écrit ; bubblewrap 0.9.0 n'a pas de couche temporaire). Les options du kit sont celles de l'orchestrateur pour un contrôle Claude
(`construire_options` : `ANTHROPIC_BASE_URL` = le relais, `ANTHROPIC_API_KEY` = le jeton factice, variables sans repli de
modèle, `setting_sources=[]`, aucun outil).

Environnements hérités éprouvés (noms seulement au résultat) :
  A   celui que le lanceur v2 transmettait : l'environnement de la session moins les noms de clé (`environnement_sans_cles`) ;
  B   minimal : PATH, HOME, LANG ;
  A-x A moins un groupe de noms (recherche du nom qui fait la différence) ;
  V3  celui que le lanceur v3 transmet (liste de noms permis), passé par sa propre fonction.

Usage : /usr/local/bin/python3 -I -B eprouver_authentification_kit_v1.py DOSSIER_DE_TRAVAIL_NEUF
Sortie : un objet JSON (sur la sortie standard et dans le dossier de travail).
"""
import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path

DEPOT = Path("/home/user/controle-ia-travail")
LANCEUR_V2 = DEPOT / "scripts" / "lancer_course_ideation_bassins_etroits_v2.py"
LANCEUR_V3 = DEPOT / "scripts" / "lancer_course_ideation_bassins_etroits_v3.py"
JETON_FACTICE = "relais-local-sans-cle"

INTERIEUR = r'''
import asyncio, json, os, sys, threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
FACTICE = "relais-local-sans-cle"
notes = []
class H(BaseHTTPRequestHandler):
    def _rep(self):
        n = int(self.headers.get("content-length") or 0)
        if n:
            self.rfile.read(n)
        a = self.headers.get("authorization")
        notes.append({"methode": self.command, "chemin": self.path.split("?")[0],
                      "noms_en_tetes": sorted(k.lower() for k in self.headers.keys()),
                      "x_api_key_presente": self.headers.get("x-api-key") is not None,
                      "x_api_key_egale_factice": self.headers.get("x-api-key") == FACTICE,
                      "authorization_presente": a is not None,
                      "authorization_schema": (a.split(" ", 1)[0] if a else None),
                      "authorization_egale_bearer_factice": a == "Bearer " + FACTICE})
        corps = json.dumps({"type": "error", "error": {"type": "authentication_error", "message": "faux amont"}}).encode()
        self.send_response(401)
        self.send_header("content-type", "application/json")
        self.send_header("content-length", str(len(corps)))
        self.end_headers()
        self.wfile.write(corps)
    do_GET = do_POST = do_HEAD = _rep
    def log_message(self, *a):
        pass
srv = ThreadingHTTPServer(("127.0.0.1", 0), H)
threading.Thread(target=srv.serve_forever, daemon=True).start()
url = "http://127.0.0.1:%d" % srv.server_address[1]
import claude_agent_sdk as sdk
opts = sdk.ClaudeAgentOptions(
    model="claude-fable-5-1", fallback_model=None, tools=[], allowed_tools=[], max_turns=1, setting_sources=[],
    cwd=sys.argv[2], permission_mode="default",
    env={"ANTHROPIC_BASE_URL": url, "ANTHROPIC_API_KEY": FACTICE,
         "CLAUDE_CODE_NO_MODEL_FALLBACK": "true", "CLAUDE_CODE_DISABLE_REFUSAL_FALLBACK": "1"})
async def jouer():
    servis, erreur = [], None
    try:
        async for m in sdk.query(prompt="Réponds exactement OK, sans rien d'autre.", options=opts):
            servis.append(type(m).__name__ + ":" + str(getattr(m, "model", "") or ""))
    except Exception as e:
        erreur = type(e).__name__
    return servis, erreur
try:
    servis, erreur = asyncio.run(asyncio.wait_for(jouer(), 45))
except Exception as e:
    servis, erreur = [], "delai:" + type(e).__name__
json.dump({"requetes": notes, "messages": servis[:6], "erreur": erreur}, open(sys.argv[1], "w"))
'''


def charger(nom, chemin):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec)
    sys.modules[nom] = m
    spec.loader.exec_module(m)
    return m


def essayer(travail: Path, nom: str, env: dict, home: str = "vide") -> dict:
    d = travail / nom
    d.mkdir()
    sortie = d / "notes.json"
    script = d / "interieur.py"
    script.write_text(INTERIEUR, encoding="utf-8")
    if env.get("HOME", "").startswith("@DOSSIER@"):   # HOME neuf fixé par le lanceur v3 : un dossier vide de cet essai
        env = dict(env, HOME=str(d / "home"))
        (d / "home").mkdir()
    argv = ["bwrap", "--die-with-parent", "--unshare-net", "--ro-bind", "/", "/", "--dev", "/dev", "--proc", "/proc",
            "--tmpfs", "/tmp", *(["--tmpfs", "/root"] if home == "vide" else []), "--bind", str(d), str(d),
            "/usr/local/bin/python3", "-I", "-B", str(script), str(sortie), str(d)]
    try:
        p = subprocess.run(argv, env=env, capture_output=True, text=True, timeout=150, stdin=subprocess.DEVNULL)
        code = p.returncode
        err = p.stderr[-400:]
    except subprocess.TimeoutExpired:
        code, err = "delai", ""
    res = json.loads(sortie.read_text()) if sortie.exists() else {"requetes": [], "erreur": "aucune note"}
    req = res.get("requetes", [])
    resume = {"code_bwrap": code, "requetes": len(req),
              "x_api_key_egale_factice": sorted({r["x_api_key_egale_factice"] for r in req}),
              "x_api_key_presente": sorted({r["x_api_key_presente"] for r in req}),
              "authorization_schemas": sorted({str(r["authorization_schema"]) for r in req}),
              "authorization_egale_bearer_factice": sorted({r["authorization_egale_bearer_factice"] for r in req}),
              "chemins": sorted({r["chemin"] for r in req}), "messages": res.get("messages"), "erreur": res.get("erreur"),
              "noms_en_tetes_premiere_requete": req[0]["noms_en_tetes"] if req else None,
              "stderr_fin_sans_valeur": "(omis)" if err else ""}
    # verdict sur les seules requêtes d'appel de modèle (POST /v1/messages) : une sonde de connectivité sans en-tête
    # (HEAD /api/hello) n'est pas un appel
    appels = [r for r in req if r["methode"] == "POST" and r["chemin"].startswith("/v1/messages")]
    resume["appels_de_modele"] = len(appels)
    resume["autres_requetes"] = sorted({f'{r["methode"]} {r["chemin"]}' for r in req if r not in appels})
    resume["verdict"] = ("jeton factice présenté" if appels and all(r["x_api_key_egale_factice"] or
                                                                    r["authorization_egale_bearer_factice"] for r in appels)
                         else "autre authentification que le jeton factice" if appels else "aucun appel au faux amont")
    return resume


def main():
    travail = Path(sys.argv[1]).resolve()
    if travail.exists():
        raise SystemExit("le dossier de travail doit être neuf")
    travail.mkdir(parents=True)
    v2 = charger("lanceur_v2_epreuve", LANCEUR_V2)
    env_a, _ = v2.environnement_sans_cles(os.environ, travail / "pyc")
    variantes = {"A_v2": env_a, "B_minimal": {k: os.environ[k] for k in ("PATH", "HOME", "LANG") if k in os.environ}}
    groupes = {
        "CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST": ["CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST"],
        "CLAUDE_CODE_USE_CCR_V2": ["CLAUDE_CODE_USE_CCR_V2"],
        "CLAUDE_CODE_REMOTE*": [n for n in env_a if n.startswith("CLAUDE_CODE_REMOTE")],
        "ANTHROPIC_*": [n for n in env_a if n.startswith("ANTHROPIC")],
        "CCR_*": [n for n in env_a if n.startswith("CCR_")],
        "CLAUDE*_sauf_les_precedents": [n for n in env_a if n.startswith("CLAUDE")],
    }
    for n in sorted(x for x in env_a if x.startswith("CLAUDE_CODE_REMOTE")):
        groupes[n] = [n]
    for nom, noms in groupes.items():
        variantes["A_moins_" + nom] = {k: v for k, v in env_a.items() if k not in noms}
    if LANCEUR_V3.exists():
        v3 = charger("lanceur_v3_epreuve", LANCEUR_V3)
        env_v3, _ = v3.environnement_permis(os.environ, travail / "pyc", Path("@DOSSIER@/home"))
        variantes["V3"] = env_v3
    out = {"jeton_factice": "relais-local-sans-cle (constante publique de pole/relais.py)", "variantes": {}}
    for home in ("vide", "lecture_seule"):
        for nom, env in variantes.items():
            if home == "lecture_seule" and nom not in ("A_v2", "B_minimal", "A_moins_CLAUDE_CODE_REMOTE*", "V3"):
                continue
            cle = f"{nom}|home_{home}"
            out["variantes"][cle] = {"noms_transmis": len(env), "noms_claude_anthropic_ccr": sorted(
                n for n in env if n.startswith(("CLAUDE", "ANTHROPIC", "CCR"))), **essayer(travail, cle.replace("|", "-"),
                                                                                           env, home)}
            print(json.dumps({cle: out["variantes"][cle]["verdict"]}, ensure_ascii=False), file=sys.stderr, flush=True)
    texte = json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True)
    (travail / "resultat.json").write_text(texte + "\n", encoding="utf-8")
    print(texte)


if __name__ == "__main__":
    main()
