"""Fabrique le brouillon 6 de l'ordre de l'étalonnage depuis le brouillon 5, par deux remplacements à ancre comptée.
Demande de la mère (2026-11-21, vers 20:19Z) : (1) ligne « Exécutante » : l'exécutante neuve session_01Qi7Gr6cZ3HczDtN4UYdPN9
(mandat registres/iib-executante/mandat-executante-iib-v2.md sur main, b26e66ee…) ;
(2) chemin des correctifs du distillateur dans la table des correctifs : `code-v5/distillateur-v5/correctifs/…`.
Rien d'autre. Usage : python3 fabriquer-ordre-etalonnage-ii-b-v5-brouillon6-v1.py (depuis ce dossier)."""
import hashlib, pathlib

ICI = pathlib.Path(__file__).resolve().parent
SOURCE, CIBLE = ICI / "ordre-etalonnage-ii-b-v5-brouillon5.md", ICI / "ordre-etalonnage-ii-b-v5-brouillon6.md"
EMPREINTE_SOURCE = "3bde656a"

t = SOURCE.read_text(encoding="utf-8")
assert hashlib.sha256(t.encode("utf-8")).hexdigest().startswith(EMPREINTE_SOURCE), "brouillon 5 inattendu"
REMPLACEMENTS = [
    ("| Exécutante | `session_013QMaymHf2YhybDs3MJ62xr` ;",
     "| Exécutante | `session_01Qi7Gr6cZ3HczDtN4UYdPN9` (branche `claude/iib-executante-v5`, mandat `registres/iib-executante/mandat-executante-iib-v2.md` sur `main`, `b26e66ee…` ; l'exécutante de la première course, `session_013QMaymHf2YhybDs3MJ62xr`, n'est plus joignable) ;", 1),
    ("| `distillateur-v5/correctifs/", "| `code-v5/distillateur-v5/correctifs/", 3),
]
for ancien, nouveau, n in REMPLACEMENTS:
    assert t.count(ancien) == n, (ancien, t.count(ancien))
    t = t.replace(ancien, nouveau)
CIBLE.open("x", encoding="utf-8").write(t)
print(CIBLE.name, hashlib.sha256(t.encode("utf-8")).hexdigest())
