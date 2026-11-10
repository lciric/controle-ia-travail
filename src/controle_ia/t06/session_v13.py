"""Chaîne de session de T0.6, v13 (lanceur `scripts/lancer_t06_v14.sh`, amorce `scripts/amorce_instance_t06_v12.sh` ; nom neuf, R12 : `session_v12.py` et les
précédents restent tels quels).

Seule différence avec `session_v12.py` : **en mode course aussi, aucun identifiant de GO n'est écrit en dur**. La chaîne v13 vérifiait la course par `session_v2 go`
(`session.verifier_go` : GO-2026-11-02-28 seulement, plafond exact de 200 USD) ; ici la ligne de la course est celle de la configuration (`go_id`) :
- `go_de_la_configuration(config, registre, go_id, jour)` : `go_id` lisible (GO-AAAA-MM-JJ-NN) ; la configuration porte ce même `go_id` (sinon refus) ; la ligne est
  lue au registre par `session_v12.ligne_go_calcul` (présente, type « calcul », accordée par Lazar, non échue au jour donné, non révoquée, extensions conformes) ;
  le plafond de la configuration (`plafond_usd`) est un nombre fini strictement positif **au plus égal au plafond de la ligne** ;
- `calendrier_de_la_configuration(config, registre, go_id, jour)` : la même vérification, puis `session_v3.verifier_calendrier_v3` au GO de la configuration et au
  plafond de sa ligne (L11 : `calendrier.fin_go_utc` = lendemain 00:00 UTC de l'échéance de la ligne ; dernier jour de création avant la fin du GO ; jour donné ≤
  dernier jour de création) ;
- `go_de_la_course(texte_prereg, lire)` : identifiant de la ligne de la course, lu dans la configuration citée **une seule fois** par le préenregistrement (« Chemin de
  la configuration de T0.6 ») ; sert à refuser une épreuve à blanc jouée sous la ligne de la course, sans identifiant en dur.
Toute vérification manquée lève `GardeSession` ; en ligne de commande : code 1 et le motif sur la dernière ligne, jamais un repli (R5). Bibliothèque standard seule ;
aucun appel au réseau ni à l'outil de location (`go-course-git` lit un commit du dépôt local par `git show`).

    python -I -m controle_ia.t06.session_v13 go-config CONFIG.json REGISTRE_GO.md GO_ID [AAAA-MM-JJ]
        imprime « GO_ID conforme (plafond de la ligne L USD, accord → échéance) ; plafond de la configuration P ≤ L »
    python -I -m controle_ia.t06.session_v13 calendrier-config CONFIG.json REGISTRE_GO.md GO_ID [AAAA-MM-JJ]
        imprime « fin_go_utc_s=… dernier_jour_creation=… echeance_go=… plafond_ligne=L »
    python -I -m controle_ia.t06.session_v13 go-course PREREG.md RACINE            (configuration citée lue sous RACINE ; imprime l'identifiant)
    python -I -m controle_ia.t06.session_v13 go-course-git DEPOT COMMIT PREREG     (texte et configuration lus dans COMMIT par `git show` ; imprime l'identifiant)
    autres sous-commandes : celles de `session_v12` (`go-ligne`, `plafond-ligne`, `plafond`, puis `session_v11`, …).
"""
from __future__ import annotations

import json
import math
import re
import subprocess
import sys
from datetime import date
from decimal import Decimal
from pathlib import Path

from . import session_v2 as s2
from . import session_v3 as s3
from . import session_v12 as s12
from .session import GardeSession

ligne_go_calcul, plafond_de_la_ligne, verifier_plafond_epreuve = s12.ligne_go_calcul, s12.plafond_de_la_ligne, s12.verifier_plafond_epreuve
CITATION_CONFIG = re.compile(r"Chemin de la configuration de T0\.6 : `([^`]+)`")


def _plafond_configuration(config: dict) -> Decimal:
    p = config.get("plafond_usd")
    if isinstance(p, bool) or not isinstance(p, (int, float)) or not math.isfinite(p) or not p > 0:
        raise GardeSession(f"plafond_usd de la configuration {p!r} : nombre fini strictement positif attendu")
    return Decimal(repr(float(p)))


def go_de_la_configuration(config: dict, registre, go_id: str, jour: date | None = None) -> dict:
    """La ligne `go_id` (reçue de l'environnement ou du lanceur) est celle de la configuration, conforme au registre, et le plafond de la configuration ne dépasse pas
    celui de la ligne. Rend la ligne (`session_v3.verifier_go_v3`) plus `plafond_configuration`."""
    if not isinstance(config, dict):
        raise GardeSession("configuration illisible (objet JSON attendu)")
    if not s3.ID_GO.fullmatch(str(go_id)):
        raise GardeSession(f"identifiant de GO illisible : {go_id!r} (GO-AAAA-MM-JJ-NN attendu)")
    goc = config.get("go_id")
    if goc != go_id:
        raise GardeSession(f"go_id de la configuration ({goc!r}) ≠ GO reçu ({go_id})")
    p = _plafond_configuration(config)
    ligne = ligne_go_calcul(registre, go_id, jour)
    limite = Decimal(repr(float(ligne["plafond_usd"])))
    if p > limite:
        raise GardeSession(f"plafond de la configuration {p} > plafond {limite} de la ligne {go_id} du registre ({ligne['accorde']} → {ligne['echeance']})")
    return {**ligne, "plafond_configuration": float(p)}


def calendrier_de_la_configuration(config: dict, registre, go_id: str, jour: date | None = None) -> dict:
    """`go_de_la_configuration`, puis le calendrier de la configuration (L11) contre la même ligne, à son propre plafond."""
    ligne = go_de_la_configuration(config, registre, go_id, jour)
    cal = s3.verifier_calendrier_v3(config, registre, go_id, ligne["plafond_usd"], jour)
    return {**cal, "plafond_ligne": ligne["plafond_usd"]}


def go_de_la_course(texte_prereg: str, lire) -> str:
    """Identifiant de GO de la configuration citée une seule fois par le texte (`lire(chemin)` rend le texte de la configuration)."""
    cites = CITATION_CONFIG.findall(texte_prereg)
    if len(cites) != 1:
        raise GardeSession(f"chemin de la configuration de T0.6 cité {len(cites)} fois dans le préenregistrement (une fois attendue)")
    try:
        config = json.loads(lire(cites[0]))
    except (OSError, ValueError, subprocess.CalledProcessError) as e:
        raise GardeSession(f"configuration citée {cites[0]} illisible ({type(e).__name__})") from None
    g = config.get("go_id") if isinstance(config, dict) else None
    if not (isinstance(g, str) and s3.ID_GO.fullmatch(g)):
        raise GardeSession(f"go_id de la configuration citée {cites[0]} illisible : {g!r}")
    return g


def _git_show(depot: str, commit: str, chemin: str) -> str:
    if not re.fullmatch(r"[0-9a-f]{40}", commit):
        raise GardeSession(f"commit illisible : {commit!r} (40 caractères hexadécimaux)")
    r = subprocess.run(["git", "-C", depot, "show", f"{commit}:{chemin}"], capture_output=True, text=True, timeout=120)
    if r.returncode != 0:
        raise GardeSession(f"{chemin} absent du commit {commit[:12]}")
    return r.stdout


def _jour(argv: list[str], n: int) -> date | None:
    return date.fromisoformat(argv[n]) if len(argv) > n else None


def main(argv: list[str]) -> int:
    try:
        if len(argv) in (4, 5) and argv[0] == "go-config":
            r = go_de_la_configuration(s2._lire_json(argv[1]), argv[2], argv[3], _jour(argv, 4))
            print(f"{r['go']} conforme (plafond de la ligne {r['plafond_usd']:g} USD, {r['accorde']} → {r['echeance']}) ; "
                  f"plafond de la configuration {r['plafond_configuration']:g} ≤ {r['plafond_usd']:g}")
            return 0
        if len(argv) in (4, 5) and argv[0] == "calendrier-config":
            r = calendrier_de_la_configuration(s2._lire_json(argv[1]), argv[2], argv[3], _jour(argv, 4))
            print(f"fin_go_utc_s={r['fin_go_utc_s']} dernier_jour_creation={r['dernier_jour_creation']} echeance_go={r['echeance_go']} plafond_ligne={r['plafond_ligne']:g}")
            return 0
        if len(argv) == 3 and argv[0] == "go-course":
            racine = Path(argv[2])
            try:
                texte = Path(argv[1]).read_text(encoding="utf-8")
            except OSError:
                raise GardeSession(f"préenregistrement {argv[1]} absent") from None
            print(go_de_la_course(texte, lambda c: (racine / c).read_text(encoding="utf-8")))
            return 0
        if len(argv) == 4 and argv[0] == "go-course-git":
            depot, commit, prereg = argv[1:4]
            print(go_de_la_course(_git_show(depot, commit, prereg), lambda c: _git_show(depot, commit, c)))
            return 0
    except (GardeSession, ValueError) as e:                       # ValueError : jour illisible ; jamais un repli
        print(str(e))
        return 1
    if argv and argv[0] in ("go-config", "calendrier-config", "go-course", "go-course-git"):
        print(f"usage : {argv[0]} : voir l'en-tête de session_v13 (nombre d'arguments)", file=sys.stderr)
        return 2
    return s12.main(argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
