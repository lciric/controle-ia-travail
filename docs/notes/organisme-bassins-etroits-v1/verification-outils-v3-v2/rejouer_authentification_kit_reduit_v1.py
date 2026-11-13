#!/usr/bin/env python3
"""Rejeu réduit, par le vérificateur neuf (Claude Fable 5.2), de l'épreuve scellée du préparateur
`preparateur-outils-v3/eprouver_authentification_kit_v1.py` (`06ed8d4e…`) — v1, 13 novembre 2026.

Sa fonction `essayer` est reprise telle quelle (module chargé par son chemin, empreinte vérifiée) : chaque essai tourne dans
`bwrap --unshare-net` (espace réseau neuf, boucle locale seule : rien ne sort du conteneur), contre le faux amont local qui
rend 401 à tout et ne note que des noms d'en-têtes et des égalités au jeton factice public. Aucun appel de modèle, aucune
dépense, aucune valeur écrite. Trois environnements seulement, `/root` vide : A (celui du v2), A moins `CLAUDE_CODE_REMOTE`
seule, V3 (fonction `environnement_permis` du lanceur v3, HOME neuf).

Garde préalable : l'espace réseau de bwrap ne doit montrer que `lo` ; sinon rien n'est joué.

Usage : /usr/local/bin/python3 -I -B rejouer_authentification_kit_reduit_v1.py DOSSIER_DE_TRAVAIL_NEUF
"""
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path

DEPOT = Path("/home/user/controle-ia-travail")
OUTIL = DEPOT / "docs/notes/organisme-bassins-etroits-v1/preparateur-outils-v3/eprouver_authentification_kit_v1.py"
EMPREINTE_OUTIL = "06ed8d4eb6413083d55d34d1173f453236f6e2e77272f74f6c22705f2c317889"
EMPREINTE_V3 = "3fabd71e63bf9f3e830ed5128cd6a92f04ca91c0b13dabcc0ac7d316e5f44b36"


def main():
    travail = Path(sys.argv[1]).resolve()
    if travail.exists():
        raise SystemExit("le dossier de travail doit être neuf")
    if hashlib.sha256(OUTIL.read_bytes()).hexdigest() != EMPREINTE_OUTIL:
        raise SystemExit("outil du préparateur d'empreinte différente")
    p = subprocess.run(["bwrap", "--die-with-parent", "--unshare-net", "--ro-bind", "/", "/", "--dev", "/dev", "--proc", "/proc",
                        "--tmpfs", "/tmp", "/bin/cat", "/proc/net/dev"], capture_output=True, text=True, timeout=30)
    interfaces = sorted(l.split(":")[0].strip() for l in p.stdout.splitlines()[2:])
    if p.returncode != 0 or interfaces != ["lo"]:
        raise SystemExit(f"espace réseau non isolé (code {p.returncode}, interfaces {interfaces}) : rien joué")
    travail.mkdir(parents=True)
    spec = importlib.util.spec_from_file_location("outil_preparateur", OUTIL)
    o = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = o
    spec.loader.exec_module(o)
    v2 = o.charger("lanceur_v2_epreuve", o.LANCEUR_V2)
    v3 = o.charger("lanceur_v3_epreuve", o.LANCEUR_V3)
    if hashlib.sha256(o.LANCEUR_V3.read_bytes()).hexdigest() != EMPREINTE_V3:
        raise SystemExit("lanceur v3 d'empreinte différente")
    env_a, _ = v2.environnement_sans_cles(os.environ, travail / "pyc")
    env_v3, _ = v3.environnement_permis(os.environ, travail / "pyc", Path("@DOSSIER@/home"))
    variantes = {"A_v2": env_a, "A_moins_CLAUDE_CODE_REMOTE": {k: v for k, v in env_a.items() if k != "CLAUDE_CODE_REMOTE"},
                 "V3": env_v3}
    out = {"interfaces_de_l_espace_reseau": interfaces, "CLAUDE_CODE_REMOTE_dans_la_session": "CLAUDE_CODE_REMOTE" in os.environ,
           "variantes": {}}
    for nom, env in variantes.items():
        out["variantes"][nom] = {"noms_transmis": len(env), "noms_claude_anthropic_ccr": len(
            [n for n in env if n.startswith(("CLAUDE", "ANTHROPIC", "CCR"))]), **o.essayer(travail, nom, env, "vide")}
        print(json.dumps({nom: out["variantes"][nom]["verdict"]}, ensure_ascii=False), file=sys.stderr, flush=True)
    print(json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True))


if __name__ == "__main__":
    main()
