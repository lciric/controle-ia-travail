"""Contrôles de session de l'organisme retenu, v5 : ceux de `session_v1`, sauf la vérification de la configuration.

Le lanceur de session appelle `session_v1` pour le GO, le plafond de la ligne, la variante, la carte, le filtre et le choix des
offres, les instances et le préalable de création ; ces sous-commandes lisent dans la configuration des sections de la forme de
la version 1, que la configuration en version 5 porte à l'identique en mode réel (`configuration_v5.exiger_location`). Seule la
sous-commande `config` change : elle vérifie par `configuration_v5.exiger_config_v5` (prête à lancer), non par la version 1.
Usage : `python -I -B -c "… session_v5.main(sys.argv[1:])" config CONFIG.json`, ou toute sous-commande de `session_v1`.

**Coupure propre de l'étalonnage à 16 USD** (relevée de 12 à 16 USD par le correctif 0013, sous le plafond de 17 USD de l'étape 1
au devis scellé de la version 5 ; ligne d'accord GO-2026-11-21-70) : sous-commande
`coupure-etalonnage PHASE PROGRES.txt MAINTENANT_S PRIX_CARTE PRIX_STOCKAGE CREATION_S`, jouée par la surveillance du lanceur de
session à chaque relevé, après la garde de dépense de la ligne (55 USD), qui reste. La dépense comptée est celle de la machine
depuis le début de l'amorce (première ligne « AMORCE IIB … DEMARRAGE 1 : <instant> » relevée du journal), au prix réel lu à la
création (carte et stockage) ; si cette ligne n'est pas encore relevée, elle se compte depuis la création, qui la précède (jamais
moins de dépense que la vraie). Elle ne joue que si la phase est l'étalonnage ; une phase illisible est un refus (la surveillance
arrête : aucun repli silencieux). La règle rend une ligne « ARRET coupure de l'étalonnage : … » ou « RIEN … » ; l'arrêt se fait
par l'identifiant (R10), puis la destruction par la sous-commande `destruction` du lanceur de session et ses gardes.

**Correctif 0011** : la surveillance appelle la règle par `python3 -I -B` du système, où numpy peut manquer (machine louée,
première tentative de l'étalonnage, 21 novembre : « No module named 'numpy' », par `configuration_v5` puis les lois exactes).
Le chemin de la règle ne charge donc que la bibliothèque standard et `gardes` ; `configuration_v5` n'est chargé que par la
sous-commande `config`, qui en a besoin. Rien d'autre ne change : seuil, compte, phase illisible refusée.

**Correctif 0023 — coupure effective de la machine = plafond de la ligne − dépense antérieure vraie** (mot de Lazar, GO-2026-11-22-77,
« correction étroite de la garde, option (b) » ; constat du développeur, point 1). Avant : `go` exigeait plafond de la configuration
+ dépense antérieure ≤ plafond de la ligne, ce qui refusait toute dépense antérieure au-delà de 5 USD sous une ligne de 60 et une
configuration de 55. Désormais, sous-commandes `go` et `plafond-total` de ce module (elles priment sur celles de `session_v1`) :
- la ligne reste lue et jugée comme avant (`session_v12.ligne_go_calcul` : type, accord, échéance, révocation, forme « N USD ») ;
- plafond de la configuration ≤ plafond de la ligne, et dépense antérieure < plafond de la ligne, sinon refus ;
- plafond **total** passé à la garde de dépense (`session_v3 depense`, qui retranche elle-même la dépense antérieure et le
  téléchargement) : T = min(plafond de la ligne, plafond de la configuration + dépense antérieure). La machine neuve peut donc
  dépenser au plus min(plafond de la configuration, plafond de la ligne − dépense antérieure) : jamais plus que le plafond scellé
  de la configuration, jamais un total au-delà de la ligne. À dépense antérieure ≤ ligne − configuration, rien ne change.
- coupure effective nulle (machine sans reste) : refus. Le plafond scellé de la configuration ne change pas.
"""
from __future__ import annotations

import json
import math
import re
import sys
from datetime import date, datetime, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path

from ..gardes import GardeArret

COUPURE_ETALONNAGE_USD = 16.0          # coupure propre de l'étalonnage, par une règle de la surveillance (12 relevé à 16, correctif 0013)
PHASES = ("etalonnage", "conditions", "course")
_DEBUT_AMORCE = re.compile(r"^AMORCE IIB v\d+ DEMARRAGE 1 : (\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)", re.M)


def _positif(quoi: str, v, strict: bool = False) -> float:
    try:
        x = float(v)
    except (TypeError, ValueError):
        raise GardeArret(f"coupure de l'étalonnage : {quoi} = {v!r} (nombre attendu)") from None
    if not math.isfinite(x) or x < 0 or (strict and x == 0):
        raise GardeArret(f"coupure de l'étalonnage : {quoi} = {v!r} (nombre positif attendu)")
    return x


def coupure_etalonnage(phase: str, progres: str, maintenant_s, prix_carte, prix_stockage, creation_s) -> dict:
    """Règle de la surveillance : pendant l'étalonnage, la dépense comptée depuis le début de l'amorce, au prix réel lu, atteint
    16 USD → arrêt. Hors de l'étalonnage la règle ne joue pas (la coupure de la ligne reste seule)."""
    if phase not in PHASES:
        raise GardeArret(f"coupure de l'étalonnage : phase {phase!r} illisible ({', '.join(PHASES)}) : refus, aucun repli")
    now, cree = _positif("maintenant", maintenant_s), _positif("création", creation_s)
    prix = _positif("prix de la carte", prix_carte, strict=True) + _positif("prix du stockage", prix_stockage)
    if phase != "etalonnage":
        return {"joue": False, "arret": False, "phase": phase, "seuil_usd": COUPURE_ETALONNAGE_USD}
    m = _DEBUT_AMORCE.search(progres or "")
    debut, origine = cree, "création (début de l'amorce non encore relevé)"
    if m:
        lu = datetime.strptime(m.group(1), "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).timestamp()
        if lu >= cree:                                   # un début d'amorce antérieur à la création est un artefact : la création compte
            debut, origine = lu, "début de l'amorce"
    if now < debut:
        raise GardeArret("coupure de l'étalonnage : début postérieur à maintenant")
    depense = (now - debut) / 3600.0 * prix
    return {"joue": True, "arret": depense >= COUPURE_ETALONNAGE_USD, "phase": phase, "depense_usd": round(depense, 4),
            "seuil_usd": COUPURE_ETALONNAGE_USD, "prix_usd_h": round(prix, 6), "depuis": origine, "debut_utc_s": int(debut)}


def _d(x: Decimal) -> str:
    """Écriture décimale sans exposant ni zéro final (60.0 → 60, 50.350 → 50.35)."""
    s = f"{x:f}"
    return s.rstrip("0").rstrip(".") if "." in s else s


def coupure_effective(registre, go_id: str, plafond_config, anterieure, jour: date | None = None) -> dict:
    """Correctif 0023 : ligne de GO jugée comme avant, puis plafond total T = min(ligne, configuration + antérieure) et coupure de
    la machine T − antérieure = min(configuration, ligne − antérieure). Refus : configuration > ligne, antérieure ≥ ligne, valeurs
    illisibles, non finies ou négatives. Aucun repli."""
    from ..t06 import session_v12 as s12          # bibliothèque standard seule (lu par `python3 -I` du système)
    from ..t06.session import GardeSession

    ligne = s12.ligne_go_calcul(registre, go_id, jour)
    try:
        p, a = Decimal(str(plafond_config)), Decimal(str(anterieure))
    except InvalidOperation:
        raise GardeSession(f"plafond de la configuration ({plafond_config!r}) ou dépense antérieure ({anterieure!r}) illisible") from None
    if not (p.is_finite() and a.is_finite()):
        raise GardeSession("plafond de la configuration ou dépense antérieure non fini")
    if p <= 0 or a < 0:
        raise GardeSession(f"plafond de la configuration {p} (> 0 exigé) ou dépense antérieure {a} (≥ 0 exigé)")
    limite = Decimal(repr(float(ligne["plafond_usd"])))
    if p > limite:
        raise GardeSession(f"plafond de la configuration {_d(p)} > plafond de la ligne {_d(limite)} ({go_id}) : refus")
    if a >= limite:
        raise GardeSession(f"dépense antérieure {_d(a)} ≥ plafond de la ligne {_d(limite)} ({go_id}) : aucune coupure effective, refus")
    total = min(limite, p + a)
    machine = total - a
    if machine <= 0:                               # garde redondante (a < limite et p > 0 l'impliquent) : jamais un repli
        raise GardeSession(f"coupure effective de la machine {machine} ≤ 0 : refus")
    return {**ligne, "plafond_config_usd": p, "anterieure_usd": a, "plafond_ligne_usd": limite, "plafond_total_usd": total,
            "coupure_machine_usd": machine,
            "plafond_verifie": (f"coupure effective de la machine {_d(machine)} = min(plafond de la configuration {_d(p)}, plafond de la ligne "
                                f"{_d(limite)} − dépense antérieure {_d(a)}) ; total {_d(total)} ≤ {_d(limite)} (plafond de la ligne {go_id} du registre, "
                                f"{ligne['accorde']} → {ligne['echeance']}) ; correctif 0023")}


def ligne_de_coupure(r: dict) -> str:
    if not r["joue"]:
        return f"RIEN : phase {r['phase']} : la règle de coupure de l'étalonnage ne joue pas"
    if r["arret"]:
        return (f"ARRET coupure de l'étalonnage : dépense comptée {r['depense_usd']:.2f} USD ≥ {r['seuil_usd']:g} USD (depuis : {r['depuis']} ; "
                f"{r['prix_usd_h']:g} USD/h, prix réel lu) : rapatrier ce qui est versé, arrêter l'instance par son identifiant (R10), puis "
                "la détruire par la sous-commande « destruction » ; résultats partiels consignés comme tels")
    return f"RIEN : dépense comptée de l'étalonnage {r['depense_usd']:.2f} USD < {r['seuil_usd']:g} USD (depuis : {r['depuis']})"


def verifier_config(chemin, racine=".") -> dict:
    from . import configuration_v5 as cf          # numpy (lois exactes) : chargé ici seulement, jamais par la règle de coupure

    config = json.loads(Path(chemin).read_text(encoding="utf-8"))
    return cf.exiger_config_v5(config, racine, pour_lancer=True)


def main(argv: list[str]) -> int:
    if len(argv) in (2, 3) and argv[0] == "config":
        try:
            r = verifier_config(argv[1], argv[2] if len(argv) == 3 else Path(__file__).resolve().parents[3])
        except (GardeArret, OSError, ValueError) as e:
            print(f"REFUS : {e}", file=sys.stderr)
            return 1
        print(f"configuration v5 conforme (mode {r['mode']}, nœuds {''.join(r['noeuds'][k] for k in sorted(r['noeuds']))})")
        return 0
    if argv and argv[0] == "coupure-etalonnage":
        if len(argv) != 7:
            print("REFUS : usage : coupure-etalonnage PHASE PROGRES.txt MAINTENANT_S PRIX_CARTE PRIX_STOCKAGE CREATION_S", file=sys.stderr)
            return 2
        try:
            texte = Path(argv[2]).read_text(encoding="utf-8") if Path(argv[2]).is_file() else ""
            print(ligne_de_coupure(coupure_etalonnage(argv[1], texte, *argv[3:7])))
        except (GardeArret, OSError, ValueError) as e:
            print(f"REFUS : {e}", file=sys.stderr)
            return 1
        return 0
    if argv and argv[0] in ("go", "plafond-total"):              # correctif 0023 : ces deux sous-commandes priment sur session_v1
        from ..t06.session import GardeSession

        if len(argv) not in (5, 6):
            print(f"usage : {argv[0]} REGISTRE GO_ID PLAFOND_CONFIG ANTERIEURE [AAAA-MM-JJ]", file=sys.stderr)
            return 2
        try:
            r = coupure_effective(argv[1], argv[2], argv[3], argv[4], date.fromisoformat(argv[5]) if len(argv) == 6 else None)
        except (GardeSession, ValueError) as e:                  # ValueError : jour illisible ; jamais un repli
            print(str(e))
            return 1
        if argv[0] == "go":
            print(f"{r['go']} conforme (plafond {r['plafond_usd']:g} USD, {r['accorde']} → {r['echeance']}) ; {r['plafond_verifie']}")
        else:
            print(_d(r["plafond_total_usd"]))          # exact, jamais arrondi (vérification de la contre-lecture, majeur)
        return 0
    from . import session_v1

    return session_v1.main(argv)
