"""Brouillon 2 de l'ordre v2 depuis le brouillon 1 : le seul champ de la session rempli, la vérification du correctif 0012.
Usage : python3 fabriquer-ordre-etalonnage-ii-b-v5-v2-brouillon2-v1.py (depuis ce dossier)."""
import hashlib, pathlib
ICI = pathlib.Path(__file__).resolve().parent
t = (ICI / "ordre-etalonnage-ii-b-v5-v2-brouillon1.md").read_text(encoding="utf-8")
assert hashlib.sha256(t.encode("utf-8")).hexdigest().startswith("284d9ec1"), "brouillon 1 inattendu"
a = "`<<VERIFICATION_CORRECTIF_0012>>`"
assert t.count(a) == 1
t = t.replace(a, "`brouillons/ii-b-saboteur-budget-v5/code-v5/correctif-0012/verification-v1/verification-corrections-correctif-0012-v1.md` (`5bd13368594d973d0800865ec4b0124ad455883d2d27e95de76c94929eb4dd12`), « conforme » : remarques de Fable toutes traitées, arbre `bbcd9a84a77ac667ef6f9106b19afe29ffab041f` retrouvé, 275 essais réussis")
(ICI / "ordre-etalonnage-ii-b-v5-v2-brouillon2.md").open("x", encoding="utf-8").write(t)
print(hashlib.sha256(t.encode("utf-8")).hexdigest())
