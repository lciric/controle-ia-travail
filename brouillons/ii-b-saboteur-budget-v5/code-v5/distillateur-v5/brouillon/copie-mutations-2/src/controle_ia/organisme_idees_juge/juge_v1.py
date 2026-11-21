"""Accès au juge réel de la copie empreintée `94bfd92` (lecture seule, par import ; R-2886).

Le préenregistrement de l'idée 1.2 exige que les richesses soient calculées par le code du juge
(`nul_filles_v2.evaluer_v2`, nul `nul_v8.membres_archive_v8`, règle `cycle.appliquer_multiplicite`, grammaire
`selection_pari`). Ce module :
- vérifie, avant tout import, l'empreinte de chaque module de la copie qu'il charge, contre la liste de la copie
  (`empreintes-copie-v1.txt`, elle-même vérifiée contre son compagnon et contre l'empreinte citée par le texte scellé)
  et, pour les cinq fichiers que le texte cite par empreinte entière, contre ces empreintes ;
- interdit l'écriture de fichiers de code compilé (`sys.dont_write_bytecode`) : rien n'est écrit sous `docs/` ;
- insère le chemin de la copie en tête de `sys.path`, importe le paquet `pole`, et vérifie que chaque module importé
  vient bien de la copie (aucun paquet homonyme ailleurs).
Aucun fichier de la copie n'est lancé comme programme. Tout écart lève `GardeArret` (aucun repli).
"""
from __future__ import annotations

import hashlib
import importlib
import sys
from pathlib import Path

from ..gardes import GardeArret

RACINE_DEPOT = Path(__file__).resolve().parents[3]
DOSSIER_COPIE = RACINE_DEPOT / "docs" / "notes" / "organisme-courbe-dose-reponse-v1" / "code-organisme-94bfd92"
DOSSIER_ORCHESTRATEUR = DOSSIER_COPIE / "orchestrator"
LISTE_EMPREINTES = DOSSIER_COPIE / "empreintes-copie-v1.txt"
# Empreintes entières citées par le texte scellé (en-tête, « juge, copie 94bfd92 »).
EMPREINTE_LISTE_CITEE = "0153e02d4522fe21eb1cf52985574eba38b5f260f7a3a08183d63589f29f32df"
EMPREINTES_CITEES = {
    "orchestrator/pole/a_blanc_v59.py": "606aa8b4fcc38786b38cf2954da46533eed9384232a56100d22ff30b8ce0826c",
    "orchestrator/pole/nul_filles_v2.py": "0ed9b4adbcddc4ad77a1c97d5cbd5706f14926e9c47fe96ce2bab3221a138910",
    "orchestrator/pole/nul_v8.py": "cc452aafd17121a7c0ec42829eea47063ffee1f6cdf7f642e264d528f976b888",
    "orchestrator/pole/cycle.py": "798f039042e3ee1f18df5c566f5a0ddee5dac5c98225c8ce621e267174c8ee18",
    "orchestrator/pole/selection_pari.py": "359928110d757cd54cc0d2773910c7360895b68cac5d17e0e4b4e9933ef306bc",
}
# Modules chargés (fermeture des imports de ceux qu'on emploie : selection_pari, nul_filles_v2, nul_v8, cycle,
# controles_pari ; `a_blanc_v59` n'est jamais importé : son montage est relu par analyse syntaxique dans les essais).
MODULES = ("__init__", "outils", "caviardage", "fiche", "selection_pari", "cycle", "memoire", "nul_v8",
           "nul_filles_v2", "controles_pari")


def _sha256(chemin: Path) -> str:
    return hashlib.sha256(chemin.read_bytes()).hexdigest()


def lire_liste(chemin: Path = LISTE_EMPREINTES) -> dict[str, str]:
    lignes = [l for l in chemin.read_text(encoding="utf-8").splitlines() if l.strip()]
    sortie = {}
    for l in lignes:
        h, _, nom = l.partition("  ")
        if len(h) != 64 or not nom:
            raise GardeArret(f"{chemin} : ligne illisible {l!r}")
        sortie[nom] = h
    return sortie


def verifier_copie(dossier_copie: Path = DOSSIER_COPIE) -> dict[str, str]:
    """Vérifie la liste d'empreintes de la copie, puis chaque module chargé ; rend {chemin relatif: empreinte}."""
    liste = dossier_copie / "empreintes-copie-v1.txt"
    if not liste.is_file():
        raise GardeArret(f"{liste} absente : copie du juge introuvable")
    h_liste = _sha256(liste)
    if h_liste != EMPREINTE_LISTE_CITEE:
        raise GardeArret(f"liste d'empreintes de la copie {h_liste[:12]}… ≠ empreinte citée par le texte scellé")
    compagnon = Path(str(liste) + ".sha256")
    if not compagnon.is_file() or compagnon.read_text(encoding="utf-8").split()[0] != h_liste:
        raise GardeArret(f"{liste} : compagnon absent ou différent")
    attendues = lire_liste(liste)
    sortie = {}
    for nom in MODULES:
        rel = f"orchestrator/pole/{nom}.py"
        chemin = dossier_copie / rel
        if rel not in attendues:
            raise GardeArret(f"{rel} absent de la liste d'empreintes de la copie")
        if not chemin.is_file():
            raise GardeArret(f"{chemin} absent sur disque")
        h = _sha256(chemin)
        if h != attendues[rel]:
            raise GardeArret(f"{rel} : empreinte {h[:12]}… ≠ liste de la copie {attendues[rel][:12]}…")
        if rel in EMPREINTES_CITEES and h != EMPREINTES_CITEES[rel]:
            raise GardeArret(f"{rel} : empreinte {h[:12]}… ≠ empreinte citée par le texte scellé")
        sortie[rel] = h
    for rel, h in EMPREINTES_CITEES.items():  # a_blanc_v59 : vérifié aussi, bien que jamais importé
        if _sha256(dossier_copie / rel) != h:
            raise GardeArret(f"{rel} : empreinte différente de celle citée par le texte scellé")
        sortie[rel] = h
    return sortie


class Juge:
    """Modules du juge réel, chargés une fois par processus."""

    def __init__(self, sp, nf, nul_v8, cycle, controles_pari, outils, empreintes):
        self.sp, self.nf, self.nul_v8, self.cycle, self.controles_pari, self.outils = sp, nf, nul_v8, cycle, controles_pari, outils
        self.empreintes = empreintes


_JUGE: Juge | None = None


def charger() -> Juge:
    global _JUGE
    if _JUGE is not None:
        return _JUGE
    empreintes = verifier_copie()
    sys.dont_write_bytecode = True  # aucun fichier compilé sous docs/ (l'arbre scellé resterait sinon « non intact »)
    chemin = str(DOSSIER_ORCHESTRATEUR)
    deja = sys.modules.get("pole")
    if deja is not None and Path(getattr(deja, "__file__", "")).resolve().parent != DOSSIER_ORCHESTRATEUR / "pole":
        raise GardeArret(f"un paquet « pole » étranger est déjà chargé : {getattr(deja, '__file__', None)}")
    if chemin not in sys.path:
        sys.path.insert(0, chemin)
    mods = {}
    for nom in ("selection_pari", "nul_filles_v2", "nul_v8", "cycle", "controles_pari", "outils"):
        mods[nom] = importlib.import_module(f"pole.{nom}")
    for nom, mod in list(sys.modules.items()):
        if nom == "pole" or nom.startswith("pole."):
            origine = Path(mod.__file__).resolve()
            if DOSSIER_ORCHESTRATEUR.resolve() not in origine.parents:
                raise GardeArret(f"module {nom} chargé hors de la copie : {origine}")
            rel = str(origine.relative_to(DOSSIER_COPIE.resolve()))
            if rel not in empreintes:
                raise GardeArret(f"module {nom} ({rel}) chargé sans empreinte vérifiée")
    _JUGE = Juge(mods["selection_pari"], mods["nul_filles_v2"], mods["nul_v8"], mods["cycle"], mods["controles_pari"],
                 mods["outils"], empreintes)
    return _JUGE
