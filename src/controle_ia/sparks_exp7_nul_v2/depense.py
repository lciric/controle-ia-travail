"""Garde de dépense mécanique de SPARKS-EXP7-NUL (addendum n° 1, « Liste d'arrêt », lignes de la dépense projetée et
de la destruction de l'instance ; contre-lecture, points 26 et 27). Bibliothèque standard seule.

Dépense projetée = dépense cumulée + pire cas restant du devis, au prix de l'offre louée :
- dépense cumulée = heures démarrées × prix horaire de la carte + heures écoulées depuis la création × prix horaire du
  stockage (prix relevés au lancement, consignés au manifeste) ; la facture de Vast, quand elle est lisible, la
  remplace si elle est plus grande ;
- pire cas restant (devis de l'addendum, colonne « pire cas ») : fabrication 6 h si elle n'est pas faite ; étape 0 et
  B3, B4 sur l'étalonnage 0,5 h si elles ne sont pas faites ; redémarrages de copie restants × 0,5 h ; contrôle causal
  4 h par lots, 16 h si l'essai d'égalité des lots a échoué (état inconnu : refus, aucun repli) ; stockage jusqu'à la
  fin du 18 novembre 2026 (échéance du GO).
Refus si la projection dépasse 40 USD : ni démarrage ni redémarrage, arrêt par identifiant (R10), nœud de Lazar.
La garde ne parle jamais à Vast : elle lit un état JSON écrit par la session et rend une décision.

    python -m controle_ia.sparks_exp7_nul_v2.depense projeter ETAT.json
    python -m controle_ia.sparks_exp7_nul_v2.depense duree PRIX_CARTE PRIX_STOCKAGE [DEJA_USD]
    python -m controle_ia.sparks_exp7_nul_v2.depense instance ETAT.json
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

PLAFOND_USD = 40.0
FIN_STOCKAGE = datetime(2026, 11, 19, 0, 0, tzinfo=timezone.utc)        # fin du 18 novembre (échéance du GO)
NOEUD_DESTRUCTION = datetime(2026, 11, 16, 0, 0, tzinfo=timezone.utc)   # 16 novembre sans fin du causal en vue
H_FABRICATION, H_ETAPE0, H_REDEMARRAGE, H_CAUSAL_LOTS, H_CAUSAL_SANS_LOTS = 6.0, 0.5, 0.5, 4.0, 16.0
PHASES = ("fabrication", "etape0", "causal")


class GardeDepense(RuntimeError):
    pass


def _instant(s: str) -> datetime:
    try:
        d = datetime.fromisoformat(s.replace("Z", "+00:00"))
    except (AttributeError, ValueError):
        raise GardeDepense(f"instant illisible {s!r}") from None
    if d.tzinfo is None:
        raise GardeDepense(f"instant sans fuseau {s!r} (UTC attendu)")
    return d


def _nombre(e: dict, k: str, *, positif: bool = False) -> float:
    v = e.get(k)
    if isinstance(v, bool) or not isinstance(v, (int, float)) or v < 0 or (positif and v <= 0):
        raise GardeDepense(f"{k} : nombre {'strictement positif' if positif else 'positif'} attendu, {v!r}")
    return float(v)


def projeter(etat: dict, maintenant: datetime | None = None) -> dict:
    """Décision de la garde : {"projection_usd", "cumulee_usd", "restant_usd", "detail", "poursuite"}."""
    now = maintenant or (_instant(etat["maintenant"]) if "maintenant" in etat else datetime.now(timezone.utc))
    p_carte = _nombre(etat, "prix_heure_carte", positif=True)
    p_stock = _nombre(etat, "prix_heure_stockage")
    h_dem = _nombre(etat, "heures_demarrees")
    cree = _instant(etat["cree_le"]) if etat.get("cree_le") else now          # pas encore créée : rien d'écoulé
    if cree > now:
        raise GardeDepense("création postérieure à maintenant")
    h_ecoulees = (now - cree).total_seconds() / 3600
    cumulee = h_dem * p_carte + h_ecoulees * p_stock
    facture = etat.get("facture_usd")
    if facture is not None:
        cumulee = max(cumulee, _nombre(etat, "facture_usd"))
    faites = set(etat.get("phases_faites", []))
    if not faites <= set(PHASES):
        raise GardeDepense(f"phases inconnues : {sorted(faites - set(PHASES))}")
    restants = etat.get("redemarrages_restants")
    if isinstance(restants, bool) or not isinstance(restants, int) or restants < 0:
        raise GardeDepense(f"redemarrages_restants : entier positif attendu, {restants!r}")
    h = {"fabrication": 0.0 if "fabrication" in faites else H_FABRICATION,
         "etape0": 0.0 if "etape0" in faites else H_ETAPE0,
         "copies": restants * H_REDEMARRAGE}
    if "causal" in faites:
        h["causal"] = 0.0
    else:
        eg = etat.get("egalite_lots")
        if eg is True:
            h["causal"] = H_CAUSAL_LOTS
        elif eg is False:
            h["causal"] = H_CAUSAL_SANS_LOTS
        else:
            raise GardeDepense("état de l'essai d'égalité des lots inconnu : aucune projection (aucun repli)")
    h_stock = max(0.0, (FIN_STOCKAGE - max(now, cree)).total_seconds() / 3600)
    restant = sum(h.values()) * p_carte + h_stock * p_stock
    proj = cumulee + restant
    return {"projection_usd": round(proj, 4), "cumulee_usd": round(cumulee, 4), "restant_usd": round(restant, 4),
            "detail": {"heures_carte": h, "heures_stockage_restantes": round(h_stock, 3)},
            "plafond_usd": PLAFOND_USD, "poursuite": proj <= PLAFOND_USD}


def exiger(etat: dict, maintenant: datetime | None = None) -> dict:
    r = projeter(etat, maintenant)
    if not r["poursuite"]:
        raise GardeDepense(f"dépense projetée {r['projection_usd']:.2f} USD > {PLAFOND_USD:g} USD : ni démarrage ni "
                           "redémarrage ; arrêt par identifiant (R10), consigné, nœud de Lazar")
    return r


def duree_max_minutes(prix_carte: float, prix_stockage: float, maintenant: datetime | None = None,
                      deja_usd: float = 0.0) -> int:
    """Borne de l'amorce : 90 % de (plafond − déjà dépensé − stockage projeté jusqu'à l'échéance), au prix horaire de la
    carte, au plus 24 h."""
    if prix_carte <= 0 or prix_stockage < 0 or deja_usd < 0:
        raise GardeDepense("prix ou dépense illisibles")
    now = maintenant or datetime.now(timezone.utc)
    stock = max(0.0, (FIN_STOCKAGE - now).total_seconds() / 3600) * prix_stockage
    libre = PLAFOND_USD - deja_usd - stock
    return int(max(0.0, min(24 * 60, 0.9 * libre / prix_carte * 60)))


def decision_instance(etat: dict, maintenant: datetime | None = None) -> dict:
    """Ligne de la destruction : contrôle causal fini → destruction (sorties scellées copiées d'abord) ; à partir du 16
    novembre sans fin en vue → nœud de Lazar ; à l'échéance (fin du 18) sans réponse → destruction. Sinon l'instance
    arrêtée est « en tâche » (garde du disque) : la routine de reprise ne la détruit pas."""
    now = maintenant or (_instant(etat["maintenant"]) if "maintenant" in etat else datetime.now(timezone.utc))
    if "causal" in set(etat.get("phases_faites", [])):
        if not etat.get("sorties_copiees"):
            return {"action": "copier", "raison": "contrôle causal fini : copier les sorties scellées, puis détruire"}
        return {"action": "detruire", "raison": "contrôle causal fini, sorties copiées"}
    if now >= FIN_STOCKAGE:
        return {"action": "detruire", "raison": "échéance du GO atteinte sans réponse de Lazar"}
    if now >= NOEUD_DESTRUCTION:
        return {"action": "noeud", "raison": "16 novembre sans fin du contrôle causal : prolongation du GO ou destruction"}
    return {"action": "garder", "raison": "instance en tâche (disque gardé entre deux redémarrages)"}


def main(argv: list[str]) -> int:
    try:
        if argv[0] == "projeter":
            r = exiger(json.loads(Path(argv[1]).read_text(encoding="utf-8")))
            print(f"DEPENSE CONFORME : projection {r['projection_usd']:.2f} USD ≤ {PLAFOND_USD:g} USD "
                  f"(cumulée {r['cumulee_usd']:.2f}, restant {r['restant_usd']:.2f})")
        elif argv[0] == "duree":
            print(duree_max_minutes(float(argv[1]), float(argv[2]), deja_usd=float(argv[3]) if len(argv) > 3 else 0.0))
        elif argv[0] == "instance":
            r = decision_instance(json.loads(Path(argv[1]).read_text(encoding="utf-8")))
            print(f"INSTANCE {r['action']} : {r['raison']}")
        else:
            raise IndexError
    except (GardeDepense, IndexError, ValueError, KeyError, OSError) as err:
        print(f"DEPENSE REFUSÉE : {err}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
