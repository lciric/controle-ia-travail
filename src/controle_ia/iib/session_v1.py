"""Chaîne de session de (ii-b), v1 (conception, section 10 : `scripts/lancer_iib_v1.sh`, `iib/session_v1.py`, tirés de
`lancer_t06_v13.sh` et `t06/session_v12.py`). Bibliothèque standard seule (lue par `python3 -I` hors de l'environnement de calcul).
Écrite et éprouvée à blanc, jamais lancée par son développeur : toutes ses lignes de GO sont lues dans un registre, factice en essai.

- `verifier_go_iib(registre, go_id, plafond, anterieure, jour)` : ligne de GO lue par son identifiant (type « calcul », accordée par
  Lazar, non échue au jour donné, non révoquée, extensions conformes : `session_v12.ligne_go_calcul`) ; plafond de la configuration +
  dépense antérieure ≤ plafond de la ligne (`session_v12.verifier_plafond_epreuve`) ;
- `verifier_variante(config, plafond_ligne)` : la configuration nomme la variante A ou B (M7, non tranchée) et le plafond de la ligne
  du registre égale celui de cette variante (80 ou 60 USD) ; le code n'en choisit aucune ;
- `verifier_carte(config, carte)` : « relance » (H200 NVL) seulement si la variante permet le repli (A) ; en B, fenêtre A100 vide =
  nœud ;
- `verifier_instances_iib(inventaire)` : seule une instance d'étiquette commençant par `iib` bloque la création ; les autres (7b,
  A1-v4, instances arrêtées) ne sont ni comptées comme bloquantes ni touchées ;
- `verifier_creation_7b(registre_decisions, config)` : la ligne de registre de la création de 7b citée par la configuration
  (`prealables.ligne_registre_creation_7b`, marqueur `<<LIGNE_REGISTRE_CREATION_7B>>`) figure au registre des décisions (une ligne
  qui la contient, exactement) ; sinon « 7b non créée » : refus ;
- `verifier_config(config)` : `configuration_v1.exiger_config_iib_v1` (le mode réel refuse tant qu'un marqueur reste).
Toute vérification manquée lève `GardeSession` ; en ligne de commande : code 1 et le motif sur la dernière ligne, jamais un repli.

    python3 -I -B -c "…session_v1.main…" go REGISTRE GO_ID PLAFOND ANTERIEURE [AAAA-MM-JJ]
    … plafond-ligne REGISTRE GO_ID [AAAA-MM-JJ] | variante CONFIG PLAFOND_LIGNE | carte CONFIG course|relance
    … instances INVENTAIRE.json | creation-7b REGISTRE_DECISIONS CONFIG | config CONFIG
    autres sous-commandes : celles de `session_v12` (filtre, choisir, presente, seule, …).
"""
from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

from ..gardes import GardeArret
from ..t06 import session_v2 as s2
from ..t06 import session_v12 as s12
from ..t06.session import GardeSession
from . import configuration_v1 as cf

ETIQUETTE_BLOQUANTE = "iib"


def verifier_go_iib(registre, go_id: str, plafond, anterieure, jour: date | None = None) -> dict:
    ligne = s12.ligne_go_calcul(registre, go_id, jour)
    return {**ligne, "plafond_verifie": s12.verifier_plafond_epreuve(plafond, anterieure, go_id, registre, jour)}


def verifier_variante(config: dict, plafond_ligne) -> str:
    try:
        v = cf.variante_de_plafond(config)
    except GardeArret as e:
        raise GardeSession(str(e)) from None
    attendu = cf.VARIANTES_PLAFOND[v]["ligne_usd"]
    if float(plafond_ligne) != float(attendu):
        raise GardeSession(f"variante {v} : la ligne de GO du registre porte {float(plafond_ligne):g} USD, la variante exige {attendu} USD")
    return v


def verifier_carte(config: dict, carte: str) -> str:
    if carte not in ("course", "relance"):
        raise GardeSession("carte : « course » (A100) ou « relance » (H200 NVL)")
    try:
        v = cf.variante_de_plafond(config)
    except GardeArret as e:
        raise GardeSession(str(e)) from None
    if carte == "relance" and not cf.VARIANTES_PLAFOND[v]["repli_h200"]:
        raise GardeSession(f"variante {v} : aucun repli H200 NVL (fenêtre A100 vide = nœud de Lazar) : aucune création")
    return v


def verifier_instances_iib(inventaire) -> dict:
    """`session_v2.verifier_instances` au préfixe `iib` : une instance de (ii-b) bloque ; les autres sont seulement comptées."""
    r = s2.verifier_instances(inventaire, ETIQUETTE_BLOQUANTE)
    return {**r, "bloquantes": 0}


def verifier_creation_7b(registre_decisions, config: dict) -> str:
    ligne = str((config.get("prealables") or {}).get("ligne_registre_creation_7b") or "").strip()
    if not ligne or "<<" in ligne or ">>" in ligne:
        raise GardeSession("ligne de registre de la création de 7b absente de la configuration : 7b non créée, refus")
    reg = Path(registre_decisions)
    if not reg.is_file():
        raise GardeSession(f"registre des décisions {registre_decisions} absent : la création de 7b n'est pas établie, refus")
    trouvees = [l for l in reg.read_text(encoding="utf-8").splitlines() if ligne in l]
    if len(trouvees) != 1:
        raise GardeSession(f"ligne de la création de 7b trouvée {len(trouvees)} fois au registre des décisions (une attendue) : "
                           "7b non créée (ou ligne ambiguë), refus")
    return ligne


def verifier_config(config: dict) -> dict:
    try:
        return cf.exiger_config_iib_v1(config)
    except GardeArret as e:
        raise GardeSession(f"configuration de (ii-b) refusée : {e}") from None


def _lire(chemin) -> dict:
    return json.loads(Path(chemin).read_text(encoding="utf-8"))


def _jour(argv, n):
    return date.fromisoformat(argv[n]) if len(argv) > n else None


def main(argv: list[str]) -> int:
    try:
        if len(argv) in (5, 6) and argv[0] == "go":
            r = verifier_go_iib(argv[1], argv[2], argv[3], argv[4], _jour(argv, 5))
            print(f"{r['go']} conforme (plafond {r['plafond_usd']:g} USD, {r['accorde']} → {r['echeance']}) ; {r['plafond_verifie']}")
            return 0
        if len(argv) in (3, 4) and argv[0] == "plafond-ligne":
            print(f"{s12.ligne_go_calcul(argv[1], argv[2], _jour(argv, 3))['plafond_usd']:g}")
            return 0
        if len(argv) == 3 and argv[0] == "variante":
            print(f"variante {verifier_variante(_lire(argv[1]), argv[2])} conforme à la ligne ({float(argv[2]):g} USD)")
            return 0
        if len(argv) == 3 and argv[0] == "carte":
            print(f"carte {argv[2]} permise (variante {verifier_carte(_lire(argv[1]), argv[2])})")
            return 0
        if len(argv) == 2 and argv[0] == "instances":
            r = verifier_instances_iib(json.loads(Path(argv[1]).read_text(encoding="utf-8") or "null"))
            print(f"aucune instance iib ; {r['total']} instance(s) sur le compte, ni comptées comme bloquantes ni touchées")
            return 0
        if len(argv) == 3 and argv[0] == "creation-7b":
            print(f"7b créée : {verifier_creation_7b(argv[1], _lire(argv[2]))}")
            return 0
        if len(argv) == 2 and argv[0] == "config":
            r = verifier_config(_lire(argv[1]))
            print(f"configuration conforme (mode {r['mode']}, variante {r['variante']}, seuil de M-1 {r['seuil_m1']})")
            return 0
    except (GardeSession, ValueError, json.JSONDecodeError, KeyError, OSError) as e:
        print(str(e))
        return 1
    if argv and argv[0] in ("go", "plafond-ligne", "variante", "carte", "instances", "creation-7b", "config"):
        print(f"usage : {argv[0]} : voir l'en-tête de iib/session_v1 (nombre d'arguments)", file=sys.stderr)
        return 2
    return s12.main(argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
