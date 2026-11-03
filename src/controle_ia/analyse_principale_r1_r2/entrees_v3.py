"""Entrées du mode « R2 seul » (code v3) : fiche `fiche-reception-r2-seul-v1` et preuve de l'arrêt de R1.

Le mode n'est permis que si R1 s'est arrêté chez le fournisseur : la fiche porte `R1: null`, un motif fermé et la preuve
(`diag/<run>/arret.json`, chemin et empreinte) ; le code vérifie que ce résultat est scellé et rattaché au manifeste du
rejeu (commande du rejeu, empreintes des textes et de l'identité citées), que son `verdict_fidelite` donne le motif
déclaré, et qu'aucune sortie de rejeu (`rejeu-activations.json`, fichiers d'activations) n'existe pour ce run. Les juges
se lisent par `entrees_v1.charger_juge`, inchangé.
"""
from __future__ import annotations

from pathlib import Path

from ..analyse_blanche_noire.entrees import exiger_empreinte, lire_json
from ..gardes import GardeArret
from ..manifeste import lire_manifeste, verifier_resultat
from ..scellement import empreinte, verifier
from . import constantes_v1 as K
from . import constantes_v3 as K3
from .entrees_v1 import CLES_ENTREE_R2, CLES_JUGE, _fichier

CLES_FICHE = {"format", "redaction", "R1", "motif_R1", "preuve_R1", "R2", "motif_R2"}


def lire_fiche_r2(racine: Path, chemin: str, scellee: bool) -> tuple[dict, str]:
    p = Path(racine) / chemin
    sha = verifier(p) if scellee else empreinte(p)
    f = lire_json(p)
    if not isinstance(f, dict) or set(f) != CLES_FICHE or f.get("format") != K3.FORMAT_FICHE:
        raise GardeArret(f"fiche de réception {chemin} : clés ou format ≠ {K3.FORMAT_FICHE}")
    if f["R1"] is not None:
        raise GardeArret("fiche : le mode R2 seul exige R1 nul (R1 livré : c'est la lecture principale qui s'applique)")
    if f["motif_R1"] not in K3.VERDICTS_ARRET.values():
        raise GardeArret(f"fiche : motif_R1 hors de la liste fermée {sorted(K3.VERDICTS_ARRET.values())}")
    _fichier(f["preuve_R1"], "preuve_R1")
    if f["R2"] is None or f["motif_R2"] is not None:
        raise GardeArret("fiche : le mode R2 seul exige R2 livré (rien d'autre à lire) et motif_R2 nul")
    r2 = f["R2"]
    if not isinstance(r2, dict) or set(r2) != CLES_ENTREE_R2:
        raise GardeArret("fiche : entrée R2 hors de forme")
    if r2["juge3b"] is None:
        raise GardeArret("fiche : R2 livré sans le juge 3B")
    for nom in ("juge3b", "juge8b"):
        e = r2[nom]
        if e is not None:
            if not isinstance(e, dict) or set(e) != CLES_JUGE:
                raise GardeArret(f"fiche : entrée R2.{nom} hors de forme")
            for k in CLES_JUGE:
                _fichier(e[k], f"R2.{nom}.{k}")
    if (r2["juge8b"] is None) != (r2["motif_juge8b"] is not None) or (
            r2["juge8b"] is None and r2["motif_juge8b"] not in K3.MOTIFS_J8_NUL):
        raise GardeArret("fiche : juge 8B nul sans motif fermé, ou motif donné avec le juge 8B livré")
    return f, sha


def verifier_arret_r1(racine: Path, preuve: dict, motif: str) -> dict:
    """Preuve de l'arrêt du rejeu : `diag/<run>/arret.json` scellé, d'empreinte égale à la fiche, rattaché au manifeste du
    rejeu ; verdict de fidélité → motif déclaré ; aucune sortie de rejeu pour ce run."""
    racine = Path(racine)
    chemin = Path(preuve["chemin"])
    if chemin.name != "arret.json" or len(chemin.parts) != 3 or chemin.parts[0] != "diag":
        raise GardeArret(f"preuve de l'arrêt de R1 : {chemin} ≠ diag/<run>/arret.json")
    run = chemin.parts[1]
    if run != K3.RUN_R1_ARRETE:
        raise GardeArret(f"preuve de l'arrêt de R1 : run {run} ≠ run arrêté cité ({K3.RUN_R1_ARRETE}, n° 247)")
    exiger_empreinte(racine, str(chemin), preuve["sha256"], "preuve de l'arrêt de R1")
    corps = verifier_resultat(racine, racine / chemin)
    if corps.get("run_id") != run:
        raise GardeArret(f"preuve de l'arrêt de R1 : résultat rattaché au run {corps.get('run_id')!r} ≠ {run}")
    m, _ = lire_manifeste(racine / "runs" / run / "manifeste.json")
    if m.get("commande") != K3.COMMANDE_REJEU:
        raise GardeArret(f"preuve de l'arrêt de R1 : run {run} n'est pas un rejeu ({m.get('commande')!r})")
    cfg = m.get("config") or {}
    if m.get("decisif") is not True or cfg.get("mode") != "reel":
        raise GardeArret(f"preuve de l'arrêt de R1 : rejeu {run} non décisif ou hors du mode « reel »")
    if (m.get("preenregistrement") or {}).get("sha256") != K.PREREG_FOURNISSEUR["sha256"]:
        raise GardeArret(f"preuve de l'arrêt de R1 : rejeu {run} lancé sous un autre texte que celui du fournisseur")
    if cfg.get("textes_sha256") != K.EMPREINTES_P3["textes"] or cfg.get("identite_sha256") != K.IDENTITE_SHA256:
        raise GardeArret("preuve de l'arrêt de R1 : textes ou identité du rejeu ≠ empreintes citées")
    verdict = corps["resultat"].get("verdict_fidelite")
    if K3.VERDICTS_ARRET.get(verdict) != motif:
        raise GardeArret(f"preuve de l'arrêt de R1 : verdict {verdict!r} ≠ motif déclaré {motif!r}")
    if (racine / "diag" / run / f"{K.RESULTAT_R1}.json").exists():
        raise GardeArret(f"run {run} : {K.RESULTAT_R1}.json présent à côté de l'arrêt : R1 n'est pas arrêté")
    autres = sorted(str(q.relative_to(racine)) for q in (racine / "diag").glob(f"*/{K.RESULTAT_R1}.json"))
    if autres:
        raise GardeArret(f"{autres[:3]} : un rejeu a versé ses sorties dans l'arbre : ce mode ne s'applique pas (nœud)")
    d = racine / "donnees" / run
    if d.exists() and any(p.name.startswith("activations-") for p in d.iterdir()):
        raise GardeArret(f"run {run} : fichiers d'activations présents : R1 n'est pas arrêté")
    return {"run": run, "verdict_fidelite": verdict, "etape": corps["resultat"].get("etape"),
            "sha256": preuve["sha256"], "manifeste_sha256": corps["manifeste_sha256"]}
