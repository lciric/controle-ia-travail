"""Idée 1.1, vue version 2 (étape 0 du 16 novembre, R-2976 : `pole/attaque_goodhart_v2.py` de la copie `a41b7b5`,
importé paresseusement par l'essai d'origine `TricheursParMorceaux.test_monde_w2_de_l_attaque_membre_du_nul_v9`, entre
dans la vue et dans la vérification de la copie, avec sa provenance v3). Version 1 : idée 1.1 (préenregistrement scellé `prereg/organisme-idee-1-1-poids-du-nul-v2.md`, `3ffe1739…`) : accès au nul v9
(copie `a41b7b5`) au-dessus du paquet `pole` de la copie `94bfd92`, et vue assemblée hors du dépôt (préalable 1).

- `verifier_copie_v9()` : empreinte de chaque fichier de la copie `a41b7b5` citée par le texte (en-tête, « Documents qui
  font foi ») contre le texte et contre son compagnon `.sha256` ;
- `charger()` : charge le juge (`juge_v1.charger`, qui vérifie la copie `94bfd92`), puis `pole/nul_v9.py` comme module
  `pole.nul_v9`, puis les deux modules neufs de ce code qui vivent dans l'espace `pole` (relatifs à `nul_v9`) :
  `nul_limite_v1.py` (La, Ld) et `morceaux_par_coupe_v1.py` (J9-Dc) ; aucun fichier de copie n'est lancé comme programme,
  aucun fichier compilé n'est écrit (`sys.dont_write_bytecode`) ;
- `noms_empruntes(J, v9)` : condition (a) du préalable 1 (les 16 noms que `nul_v9.py` emprunte aux modules de `94bfd92`) ;
- `assembler_vue(dossier)` : vue faite du paquet `pole` de `94bfd92`, de `pole/nul_v9.py`, de `demonstrations/` et
  d'`essais/`, dans un dossier **hors du dépôt**, chaque fichier vérifié par empreinte avant et après la recopie
  (condition (c), route première : les essais d'origine y sont importés, jamais lancés depuis leur dossier).
Tout écart lève `GardeArret` (aucun repli).
"""
from __future__ import annotations

import hashlib
import importlib.util
import shutil
import sys
from pathlib import Path

from ..gardes import GardeArret
from . import juge_v1

RACINE_DEPOT = juge_v1.RACINE_DEPOT
DOSSIER_V9 = RACINE_DEPOT / "docs" / "notes" / "organisme-idees-juge-v1" / "copie-nul-v9-a41b7b5"
ORCH_V9 = DOSSIER_V9 / "orchestrator"
ICI = Path(__file__).resolve().parent

# Empreintes entières citées par le texte scellé (en-tête).
EMPREINTES_V9 = {
    "orchestrator/pole/nul_v9.py": "7ae450df2482246122bf9fbcf0fa5ef30b4a7e4c6f0d09531e83af048e46ee95",
    "orchestrator/essais/test_nul_v9.py": "d42a50eb4ba9691e75e82fa4bc714a925615da80df22227fee730392015999b9",
    "orchestrator/demonstrations/banc_tricheurs_v9.py": "7e4bff5995df2a7d62a4f5a2f5f9176da614e657a55b05183325fa2fc6e24e44",
    "orchestrator/demonstrations/banc_tricheurs_v8.py": "0be47e4b5916a98499faf9c40d65369b41e3a5463d7ab444ed18ba18bba08c03",
    "orchestrator/demonstrations/banc_tricheurs_v7.py": "ef016d250b7b503f705dc95919719c68c8f968534fd901df7364a6062d67cf12",
    "PROVENANCE-complement-v1.md": "032eaeeb7d48358bdb1ef8502a40ba52b2ea1a4cce2a4eef12c822ff54f6f724",
    "PROVENANCE-complement-v2.md": "c38ba64386f05a32d077d5de65289a58704b349a063062ca91f7c7b9ab28d036",
    # complément v3 (R-2976), non cité par le texte scellé (qui ne cite que les bancs v7, v8, v9) : inscrit à l'addendum
    "orchestrator/pole/attaque_goodhart_v2.py": "3c9de8b83b6fcf198d12cacf6a6738c2fc3fe4ade9391f943b3924592959e703",
    "PROVENANCE-complement-v3.md": "a4a62a888adf273779ffe198cab9b958692106ea1208efc4aaf79bf02c63cfac",
}
COMPLEMENT_V3 = {"chemin": "docs/notes/organisme-idees-juge-v1/copie-nul-v9-a41b7b5/orchestrator/pole/attaque_goodhart_v2.py",
                 "sha256": "3c9de8b83b6fcf198d12cacf6a6738c2fc3fe4ade9391f943b3924592959e703",
                 "provenance": "docs/notes/organisme-idees-juge-v1/copie-nul-v9-a41b7b5/PROVENANCE-complement-v3.md",
                 "provenance_sha256": "a4a62a888adf273779ffe198cab9b958692106ea1208efc4aaf79bf02c63cfac"}
# Fichier de la copie non cité par empreinte dans le texte, vérifié contre son seul compagnon (il n'est pas rejoué : le
# texte ne demande que `test_nul_v9.py`).
COMPAGNON_SEUL = ("orchestrator/essais/mutations_nul_v9.py", "PROVENANCE.md")
# Condition (a) du préalable 1 : 16 noms empruntés par `nul_v9.py` (liste de [CL2], point 9, recopiée du texte).
NOMS_EMPRUNTES = {
    "nf": ("InstantsInvalides", "TYPES_AJUSTES", "valeurs_ajustees"),
    "nul_v8": ("NulV8Refuse", "description", "exiger_membres_ajustes", "membres_archive_v8"),
    "sp": ("Cache", "EngagementModifie", "TiragesNonLies", "calibrer", "plan_execution_de", "trajectoire_loi",
           "trajectoire_numerateur", "trajectoires", "verifier_plan_execution"),
}
# Modules neufs de ce code chargés dans l'espace `pole` (ils importent `nul_v9` en relatif) : nom → fichier.
MODULES_POLE_NEUFS = {"nul_limite_v1": ICI / "nul_limite_v1.py", "morceaux_par_coupe_v1": ICI / "morceaux_par_coupe_v1.py"}


def sha256(chemin: Path) -> str:
    return hashlib.sha256(Path(chemin).read_bytes()).hexdigest()


def _compagnon(chemin: Path) -> str:
    c = Path(str(chemin) + ".sha256")
    if not c.is_file():
        raise GardeArret(f"{chemin} : compagnon .sha256 absent")
    return c.read_text(encoding="utf-8").split()[0]


def verifier_copie_v9(dossier: Path = DOSSIER_V9) -> dict:
    sortie = {}
    for rel, attendu in EMPREINTES_V9.items():
        chemin = Path(dossier) / rel
        if not chemin.is_file():
            raise GardeArret(f"{chemin} absent sur disque (R11 : vérifié par chemin) : pas de jeu")
        h = sha256(chemin)
        if h != attendu:
            raise GardeArret(f"copie a41b7b5 : {rel} d'empreinte {h[:12]}… ≠ {attendu[:12]}… (texte scellé) : pas de jeu")
        if _compagnon(chemin) != h:
            raise GardeArret(f"copie a41b7b5 : {rel} ≠ son compagnon")
        sortie[rel] = h
    for rel in COMPAGNON_SEUL:
        chemin = Path(dossier) / rel
        h = sha256(chemin)
        if _compagnon(chemin) != h:
            raise GardeArret(f"copie a41b7b5 : {rel} ≠ son compagnon")
        sortie[rel] = h
    return sortie


def _charger_dans_pole(nom: str, chemin: Path, empreinte_attendue: str | None = None):
    plein = f"pole.{nom}"
    deja = sys.modules.get(plein)
    if deja is not None:
        if Path(deja.__file__).resolve() != Path(chemin).resolve():
            raise GardeArret(f"module {plein} déjà chargé depuis {deja.__file__} ≠ {chemin}")
        return deja
    if empreinte_attendue is not None and sha256(chemin) != empreinte_attendue:
        raise GardeArret(f"{chemin} : empreinte différente au chargement")
    spec = importlib.util.spec_from_file_location(plein, str(chemin))
    module = importlib.util.module_from_spec(spec)
    sys.modules[plein] = module
    try:
        spec.loader.exec_module(module)
    except BaseException:
        del sys.modules[plein]
        raise
    return module


class Vue:
    """Modules chargés : juge (`juge_v1.Juge`), v9, nul limité, morceaux par coupe ; empreintes vérifiées."""

    def __init__(self, J, v9, limite, par_coupe, empreintes):
        self.J, self.v9, self.limite, self.par_coupe, self.empreintes = J, v9, limite, par_coupe, empreintes


_VUE: Vue | None = None


def charger() -> Vue:
    global _VUE
    if _VUE is not None:
        return _VUE
    J = juge_v1.charger()
    empreintes = dict(verifier_copie_v9())
    sys.dont_write_bytecode = True
    v9 = _charger_dans_pole("nul_v9", ORCH_V9 / "pole" / "nul_v9.py", EMPREINTES_V9["orchestrator/pole/nul_v9.py"])
    if sha256(Path(v9.__file__)) != EMPREINTES_V9["orchestrator/pole/nul_v9.py"]:
        raise GardeArret("pole.nul_v9 chargé d'empreinte différente")
    if v9.nf is not J.nf or v9.nul_v8 is not J.nul_v8 or v9.sp is not J.sp:
        raise GardeArret("pole.nul_v9 n'emploie pas les modules de la copie 94bfd92 chargés par le juge")
    limite = _charger_dans_pole("nul_limite_v1", MODULES_POLE_NEUFS["nul_limite_v1"])
    par_coupe = _charger_dans_pole("morceaux_par_coupe_v1", MODULES_POLE_NEUFS["morceaux_par_coupe_v1"])
    for nom, chemin in MODULES_POLE_NEUFS.items():
        empreintes[f"src/controle_ia/organisme_idees_juge/{chemin.name}"] = sha256(chemin)
    empreintes.update({f"94bfd92:{k}": v for k, v in J.empreintes.items()})
    _VUE = Vue(J, v9, limite, par_coupe, empreintes)
    return _VUE


def noms_empruntes(J) -> dict:
    """Condition (a) du préalable 1 : rend {module: [noms absents]} (vide si tout est présent)."""
    modules = {"nf": J.nf, "nul_v8": J.nul_v8, "sp": J.sp}
    absents = {m: [n for n in noms if not hasattr(modules[m], n)] for m, noms in NOMS_EMPRUNTES.items()}
    return {m: a for m, a in absents.items() if a}


def exiger_noms_empruntes(J) -> int:
    absents = noms_empruntes(J)
    if absents:
        raise GardeArret(f"préalable 1 (a) : noms empruntés par nul_v9 absents de 94bfd92 : {absents} : pas de jeu")
    return sum(len(v) for v in NOMS_EMPRUNTES.values())


# --- vue assemblée hors du dépôt (préalable 1 (c)) ----------------------------------------------------------------------
def fichiers_de_la_vue() -> dict[str, tuple[Path, str]]:
    """{chemin dans la vue : (source, empreinte attendue)} : paquet `pole` de 94bfd92 (liste de la copie), `pole/nul_v9.py`
    de a41b7b5, `demonstrations/` (bancs v7, v8, v9) et `essais/test_nul_v9.py`."""
    liste = juge_v1.lire_liste()
    sortie = {}
    for rel, h in liste.items():
        if rel.startswith("orchestrator/pole/"):
            sortie[rel[len("orchestrator/"):]] = (juge_v1.DOSSIER_COPIE / rel, h)
    if "pole/nul_v9.py" in sortie:
        raise GardeArret("la copie 94bfd92 porte déjà un pole/nul_v9.py : vue ambiguë")
    for rel, h in EMPREINTES_V9.items():
        if rel.startswith("orchestrator/"):
            sortie[rel[len("orchestrator/"):]] = (DOSSIER_V9 / rel, h)
    return sortie


def assembler_vue(dossier: Path) -> dict:
    """Recopie la vue dans `dossier` (neuf, hors du dépôt) ; vérifie chaque fichier avant et après. Rend {chemin: empreinte}."""
    dossier = Path(dossier).resolve()
    if RACINE_DEPOT.resolve() == dossier or RACINE_DEPOT.resolve() in dossier.parents:
        raise GardeArret(f"vue assemblée sous le dépôt ({dossier}) : interdit (hors du dépôt exigé)")
    if dossier.exists():
        raise GardeArret(f"{dossier} existe déjà : vue neuve exigée")
    juge_v1.verifier_copie()
    verifier_copie_v9()
    sortie = {}
    for rel, (source, h) in sorted(fichiers_de_la_vue().items()):
        if sha256(source) != h:
            raise GardeArret(f"vue : {source} d'empreinte différente de sa liste")
        cible = dossier / rel
        cible.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, cible)
        if sha256(cible) != h:
            raise GardeArret(f"vue : recopie de {rel} altérée")
        sortie[rel] = h
    return sortie


def verifier_vue(dossier: Path, attendu: dict) -> None:
    for rel, h in attendu.items():
        if sha256(Path(dossier) / rel) != h:
            raise GardeArret(f"vue : {rel} modifié pendant le rejeu")
