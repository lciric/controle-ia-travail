"""A12 et GO cité à la création d'une machine — essai Lean, v1.

- A12 (brouillon 3, § 3.8) : aucun appel d'interface facturé tant que le GO de D-1b n'est pas inscrit dans `registres/go.md` ;
  le harnais refuse tout appel sans identifiant de GO valide. Le registre est relu **à chaque appel** (une révocation inscrite
  entre deux appels est vue).
- Création d'une machine (D-1a) : la commande cite le GO accordé (`GO-2026-11-10-13`), vérifié de même.

Lecture du registre : même table que `.claude/hooks/garde_calcul.py` (8 colonnes ; doublon admis seulement comme ligne
d'extension ; révocation = ligne de type « révocation » qui cite l'identifiant). Registre absent ou mal formé ⇒ arrêt (R5).
"""
from __future__ import annotations

import re
from datetime import date
from pathlib import Path

from controle_ia.gardes import GardeArret

LIGNE_GO = re.compile(r"^\|\s*(GO-\d{4}-\d{2}-\d{2}-\d{2})\s*\|")
RE_ID = re.compile(r"^GO-\d{4}-\d{2}-\d{2}-\d{2}$")
GO_OUTILLAGE_D1A = "GO-2026-11-10-13"


def lire_registre_go(chemin: str | Path) -> dict[str, dict]:
    chemin = Path(chemin)
    if not chemin.is_file():
        raise GardeArret(f"registre des GO {chemin} absent : aucun GO ne peut être établi")
    go: dict[str, dict] = {}
    for n, ligne in enumerate(chemin.read_text(encoding="utf-8").splitlines(), 1):
        if not LIGNE_GO.match(ligne):
            continue
        cellules = [c.strip() for c in ligne.strip().strip("|").split("|")]
        if len(cellules) != 8:
            raise GardeArret(f"registre GO mal formé ligne {n} : 8 colonnes attendues, {len(cellules)} trouvées")
        ident, accorde, typ, perimetre, plafond, echeance, par, ref = cellules
        try:
            accorde_d = date.fromisoformat(accorde)
            echeance_d = None if (echeance == "—" and typ != "calcul") else date.fromisoformat(echeance)
        except ValueError:
            raise GardeArret(f"registre GO mal formé ligne {n} : dates illisibles") from None
        if ident in go:
            premier = go[ident]
            echeance_ok = ((premier["echeance"] is None and echeance_d is None)
                           or (premier["echeance"] is not None and echeance_d is not None
                               and echeance_d <= premier["echeance"]))
            if not (perimetre.lower().startswith("extension") and typ == premier["type"] and par == "Lazar"
                    and accorde_d >= premier["accorde"] and echeance_ok):
                raise GardeArret(f"registre GO : identifiant {ident} en double")
            premier["extensions"].append(perimetre)
            continue
        go[ident] = {"accorde": accorde_d, "type": typ, "echeance": echeance_d, "par": par, "perimetre": perimetre,
                     "plafond": plafond, "ref": ref, "extensions": []}
    return go


def exiger_go_calcul(go_id: str, registre: dict[str, dict], aujourdhui: date) -> dict:
    """GO de calcul valide : présent, de type « calcul », accordé par Lazar, dans sa période, non révoqué."""
    if not isinstance(go_id, str) or not RE_ID.match(go_id):
        raise GardeArret(f"identifiant de GO absent ou mal formé : {go_id!r}")
    g = registre.get(go_id)
    if g is None:
        raise GardeArret(f"{go_id} absent de registres/go.md")
    if g["type"] != "calcul":
        raise GardeArret(f"{go_id} est un GO de type {g['type']!r}, pas « calcul »")
    if g["par"] != "Lazar":
        raise GardeArret(f"{go_id} n'est pas accordé par Lazar")
    if not (g["accorde"] <= aujourdhui <= g["echeance"]):
        raise GardeArret(f"{go_id} hors de sa période de validité ({g['accorde']} → {g['echeance']})")
    revocations = sorted(k for k, r in registre.items()
                         if r["type"] == "révocation" and (go_id in r["perimetre"] or go_id in r["ref"]))
    if revocations:
        raise GardeArret(f"{go_id} révoqué par {', '.join(revocations)}")
    return g


def autoriser_appels_modele(go_id: str, chemin_registre: str | Path, aujourdhui: date) -> dict:
    """A12 : le GO cité doit être un GO de calcul valide **du pilote D-1b** (son périmètre nomme « D-1b ») qui n'exclut pas
    les appels de modèle. Le GO de l'outillage (D-1a, « aucun appel de modèle ») est refusé."""
    g = exiger_go_calcul(go_id, lire_registre_go(chemin_registre), aujourdhui)
    perimetre = g["perimetre"]
    if "aucun appel de modèle" in perimetre.lower():
        raise GardeArret(f"A12 : {go_id} exclut tout appel de modèle (outillage D-1a) : appel refusé")
    if "D-1b" not in perimetre:
        raise GardeArret(f"A12 : {go_id} n'est pas un GO du pilote D-1b de l'essai Lean : appel refusé")
    return g


def autoriser_creation_machine(go_id: str, chemin_registre: str | Path, aujourdhui: date,
                               attendu: str = GO_OUTILLAGE_D1A) -> dict:
    """La commande de création cite le GO de l'outillage ; il doit être celui attendu et valide."""
    if go_id != attendu:
        raise GardeArret(f"création de machine : GO cité {go_id!r}, {attendu} attendu")
    return exiger_go_calcul(go_id, lire_registre_go(chemin_registre), aujourdhui)


class AppelsModeleGardes:
    """Porte de tout appel facturé : A12 (GO de D-1b relu à chaque appel), puis plafond par item et A7, puis transport.
    En D-1a il n'y a **aucun transport** : un appel qui franchirait les gardes est refusé quand même."""

    def __init__(self, go_id: str, chemin_registre: str | Path, compteur, aujourdhui=date.today, transport=None):
        self.go_id = go_id
        self.chemin_registre = Path(chemin_registre)
        self.compteur = compteur
        self.aujourdhui = aujourdhui
        self.transport = transport

    def appeler(self, ident: str, pire_cas: float, requete: dict) -> dict:
        autoriser_appels_modele(self.go_id, self.chemin_registre, self.aujourdhui())
        if self.transport is None:
            raise GardeArret("aucun transport de modèle dans l'outillage D-1a : appel refusé")
        self.compteur.lancer(ident, pire_cas)
        reponse = self.transport(requete)
        self.compteur.terminer(ident, float(reponse["cout_usd"]))
        return reponse
