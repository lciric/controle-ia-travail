"""Fabrique le brouillon 8 de l'ordre de l'étalonnage depuis le brouillon 7 : une seule correction de forme (F3 de la
revérification du brouillon 7) : la ligne barrée du § 11 nomme le champ rempli sans chevrons, pour qu'aucun contrôle ne la
prenne pour un champ restant. Rien d'autre. Usage : python3 fabriquer-ordre-etalonnage-ii-b-v5-brouillon8-v1.py."""
import hashlib, pathlib
ICI = pathlib.Path(__file__).resolve().parent
t = (ICI / "ordre-etalonnage-ii-b-v5-brouillon7.md").read_text(encoding="utf-8")
assert hashlib.sha256(t.encode("utf-8")).hexdigest().startswith("b61bc15f"), "brouillon 7 inattendu"
ancien = "| ~~`<<MOT_LAZAR_PREMIERE_ACTION_DANS_LA_PERTE>>`~~ |"
nouveau = "| ~~`MOT_LAZAR_PREMIERE_ACTION_DANS_LA_PERTE`~~ (champ rempli) |"
assert t.count(ancien) == 1 and t.count("<<MOT_LAZAR_PREMIERE_ACTION_DANS_LA_PERTE>>") == 1
t = t.replace(ancien, nouveau)
assert "<<MOT_LAZAR" not in t
(ICI / "ordre-etalonnage-ii-b-v5-brouillon8.md").open("x", encoding="utf-8").write(t)
print("ordre-etalonnage-ii-b-v5-brouillon8.md", hashlib.sha256(t.encode("utf-8")).hexdigest())
