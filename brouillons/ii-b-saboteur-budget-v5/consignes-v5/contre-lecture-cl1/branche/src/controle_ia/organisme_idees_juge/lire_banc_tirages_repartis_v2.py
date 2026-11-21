"""Lecture gelée v2 de l'idée 1.2 : la lecture v1 (`lire_banc_tirages_repartis_v1`), inchangée dans ses critères, plus
trois gardes et un rapport (contre-lecture du code `36ecc4a4…`) :

- **auto-contrôle du niveau de l'intervalle** (majeur 3) : avant toute lecture, l'intervalle rendu par
  `Reechantillonneur.intervalle` sur un vecteur de référence fixe doit égaler les quantiles 2,5 % et 97,5 % du texte,
  recalculés ici par une écriture indépendante (indices `(99, b)` tirés un à un) ; sinon `GardeArret` ;
- **sortie complète et rattachée** (mineur 2) : `journal.json` scellé exigé, `arret.json` refusé, et, si l'empreinte du
  manifeste est donnée, elle doit égaler celle que portent les sorties ;
- **membres du nul à la borne triviale** (mineur 1) : leur compte et leur liste par génération sont rapportés
  (`oracle_membres_a_la_borne_triviale`, et dans `audit_R4`), sans toucher un critère ;
- écrit `lecture-gelee-v2.json` (nom neuf, R12).
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from ..gardes import GardeArret
from ..scellement import sceller, verifier
from . import banc_tirages_repartis_v1 as B
from . import lire_banc_tirages_repartis_v1 as LB1
from . import verificateur_texte_v2 as VT

NOM_LECTURE = "lecture-gelee-v2.json"


def vecteur_de_reference() -> np.ndarray:
    return np.array([((7 * k) % 11) / 10 - 0.3 for k in range(60)], dtype=float)


def exiger_niveau_intervalle(racine: int, reechantillons: int) -> None:
    v = vecteur_de_reference()
    n = len(v)
    moyennes = np.array([v[B.generateur(racine, 99, b).integers(0, n, size=n)].mean() for b in range(reechantillons)])
    bas, haut = np.quantile(moyennes, list(VT.NIVEAU_INTERVALLE_TEXTE))
    rendu = LB1.Reechantillonneur(racine, reechantillons).intervalle(v)
    if abs(rendu["bas"] - float(bas)) > 1e-12 or abs(rendu["haut"] - float(haut)) > 1e-12:
        raise GardeArret("niveau de l'intervalle ≠ 95 % percentile du texte (quantiles 2,5 % et 97,5 %) : aucune lecture")


def membres_triviaux(sortie: dict) -> dict:
    par_gen = {t["generation"]: t.get("membres_a_la_borne_triviale") for t in sortie["oracle"]["generations"]}
    absents = sorted(g for g, v in par_gen.items() if v is None)
    signales = {g: v for g, v in par_gen.items() if v}
    return {"generations_signalees": len(signales), "detail": signales,
            "champ_absent (oracle v1)": len(absents)}


def lire(sortie: dict, racine: int, reechantillons: int = LB1.REECHANTILLONS, n_attendus: dict | None = None) -> dict:
    exiger_niveau_intervalle(racine, reechantillons)
    res = LB1.lire(sortie, racine, reechantillons, n_attendus)
    triv = membres_triviaux(sortie)
    res["oracle_membres_a_la_borne_triviale"] = triv
    if "audit_R4" in res:
        res["audit_R4"]["oracle_membres_a_la_borne_triviale"] = triv["generations_signalees"]
    res["version_lecture"] = 2
    return res


def charger_sortie_complete(dossier: Path, manifeste_sha: str | None = None) -> dict:
    dossier = Path(dossier)
    if (dossier / "arret.json").exists():
        raise GardeArret("le run s'est arrêté (arret.json présent) : aucune lecture partielle")
    try:
        verifier(dossier / "journal.json")
    except GardeArret as e:
        raise GardeArret(f"journal absent ou non scellé : run incomplet, aucune lecture ({e})") from None
    sortie = LB1.charger_sortie(dossier)
    journal = json.loads((dossier / "journal.json").read_text(encoding="utf-8"))
    if journal["manifeste_sha256"] != sortie["manifeste_sha256"] or journal["run_id"] != sortie["run_id"]:
        raise GardeArret("journal rattaché à un autre manifeste que les sorties")
    if manifeste_sha is not None and sortie["manifeste_sha256"] != manifeste_sha:
        raise GardeArret("empreinte du manifeste lu ≠ empreinte portée par les sorties : aucune lecture")
    return sortie


def ecrire_lecture(dossier: Path, racine: int, reechantillons: int = LB1.REECHANTILLONS, n_attendus: dict | None = None,
                   manifeste_sha: str | None = None) -> Path:
    dossier = Path(dossier)
    cible = dossier / NOM_LECTURE
    if cible.exists():
        raise GardeArret(f"{cible} existe déjà : R12 interdit d'écraser")
    sortie = charger_sortie_complete(dossier, manifeste_sha)
    res = lire(sortie, racine, reechantillons, n_attendus)
    corps = {"run_id": sortie["run_id"], "manifeste_sha256": sortie["manifeste_sha256"], "resultat": res}
    cible.write_text(json.dumps(corps, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    sceller(cible)
    return cible
