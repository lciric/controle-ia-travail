"""Brouillon 3 de l'ordre v2 depuis le brouillon 2 : seule la branche d'essai change (demande de la mère, 2026-11-21 vers
23:19Z) : `essai/iib-explo-v5` existe déjà sur le distant (traces de la tentative 1), sa suppression est refusée ; la branche
poussée par la machine devient `essai/iib-explo-v6` partout où l'ordre la nomme (ligne « Branche poussée », étapes 1, 5, 6,
§ 7). La phrase qui décrit la valeur par défaut du lanceur de session (un fait du code) est gardée et précisée.
Usage : python3 fabriquer-ordre-etalonnage-ii-b-v5-v2-brouillon3-v1.py (depuis ce dossier)."""
import hashlib, pathlib
ICI = pathlib.Path(__file__).resolve().parent
t = (ICI / "ordre-etalonnage-ii-b-v5-v2-brouillon2.md").read_text(encoding="utf-8")
assert hashlib.sha256(t.encode("utf-8")).hexdigest().startswith("9bf05c30"), "brouillon 2 inattendu"
DEFAUT = "branche par défaut `essai/iib-explo-v5`"
assert t.count(DEFAUT) == 1
t = t.replace(DEFAUT, "@@DEFAUT@@")
assert t.count("essai/iib-explo-v5") == 5, t.count("essai/iib-explo-v5")
t = t.replace("essai/iib-explo-v5", "essai/iib-explo-v6")
t = t.replace("@@DEFAUT@@", DEFAUT + " (remplacée sous cet ordre par `IIB_BRANCHE=essai/iib-explo-v6`, `essai/iib-explo-v5` portant déjà les traces de la tentative 1)")
assert "essai/iib-explo-v5`" in t and t.count("essai/iib-explo-v6") == 6
(ICI / "ordre-etalonnage-ii-b-v5-v2-brouillon3.md").open("x", encoding="utf-8").write(t)
print(hashlib.sha256(t.encode("utf-8")).hexdigest())
