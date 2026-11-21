"""Fabrique l'ordre de l'étalonnage en version 2 (brouillon 1) depuis le brouillon 8 de la version 1, par remplacements à
ancre comptée. Cause : premier étalonnage arrêté sur la machine pendant la suite ciblée (« 5 failed, 263 passed, 3 errors »),
avant tout chargement du modèle ; correctif 0011 (environnement de la machine) et 0012 (corrections d'après la relecture de
Fable 5.2 par l'API), arbre bbcd9a84a77ac667ef6f9106b19afe29ffab041f ; liste figée v5, 275 essais. Relance accordée d'avance
(GO-2026-11-21-87), sous GO-2026-11-21-70. Rien d'autre ne change.
Usage : python3 fabriquer-ordre-etalonnage-ii-b-v5-v2-brouillon1-v1.py (depuis ce dossier)."""
import hashlib, pathlib

ICI = pathlib.Path(__file__).resolve().parent
SOURCE, CIBLE = ICI / "ordre-etalonnage-ii-b-v5-brouillon8.md", ICI / "ordre-etalonnage-ii-b-v5-v2-brouillon1.md"
t = SOURCE.read_text(encoding="utf-8")
assert hashlib.sha256(t.encode("utf-8")).hexdigest().startswith("55de7ac1"), "brouillon 8 inattendu"

ARBRE_A, ARBRE_N = "ed9b0e48be367670cad0782ccb6fbe2d9ca41b87", "bbcd9a84a77ac667ef6f9106b19afe29ffab041f"
TETE_A, TETE_N = "c4b5115b5fe6ed679eeb61e08c779317f9cb55c5", "887561b759ded1bcadb450cedead3f29e946dda7"
EN_TETE = (
    "> **Version 2 de l'ordre (brouillon 1), fabriquée par programme depuis le brouillon 8 de la version 1** "
    "(`ordre-etalonnage-ii-b-v5-brouillon8.md`, `55de7ac17d27514a4110682c6e46bcace0540291bbb14853aaaaae5614d41a20`, intact, R12). "
    "**Cause** : le premier étalonnage sous la version 1 s'est arrêté sur la machine 61859391 pendant la suite ciblée "
    "(« 5 failed, 263 passed, 3 errors »), avant tout chargement du modèle et tout épisode, pour deux causes d'environnement "
    "(garde du mode jouet jouant dans les essais ; règle à 12 USD appelée sous l'interpréteur du système sans numpy) ; "
    "aucune sortie d'étalonnage ; machine détruite sur le mot de la mère ; environ 1,3 USD. **Ce qui change** : le code "
    "(correctifs 0011 et 0012, § 11), son arbre, la liste figée (version 5, 24 fichiers) et le nombre d'essais attendus (275). "
    "Rien d'autre : ni le texte scellé, ni le devis, ni la ligne de calcul, ni les gardes. **Relance** accordée d'avance par "
    "Lazar (`GO-2026-11-21-87`), sous `GO-2026-11-21-70`. Correctif 0011 relu par Fable 5.2 appelé par l'API "
    "(`brouillons/ii-b-saboteur-budget-v5/code-v5/correctif-0011/relecture-fable-v1/sortie-1/relecture-fable-api.md`, "
    "`ea3ffcc0e16be27bd5b3a0ff819e857d2fa9641ddd24d06e4c76797e788dd366`, « autorisable après corrections ») ; corrections "
    "(correctif 0012) vérifiées par un Opus 5.5 neuf, écart déclaré à `GO-2026-11-21-84` (R-4739) : "
    "`<<VERIFICATION_CORRECTIF_0012>>`. Les nombres « 271 » et l'arbre d'avant qui restent dans les paragraphes d'historique "
    "(statut, points rendus) décrivent la version 1 ; ce qui fait foi pour la version 2 est ce paragraphe, les lignes « Code », "
    "« Amorce », « Essais », le § 4 étape 6, le § 5 et le § 11.\n\n"
)
REMPLACEMENTS = [
    (ARBRE_A, ARBRE_N, 5),
    (TETE_A, TETE_N, 2),
    ("treize", "quinze", 4),
    ("`scripts/amorce_instance_iib_v5.sh` (`42196f90da0f104fb36a5f618a14e44ef03863d0541bb3b77f1f29f130a9e43c` à la tête du code)",
     "`scripts/amorce_instance_iib_v5.sh` (`a4686068f0cbc0733ad220675d2118c9739884b8d24b26c4a3ba40444aeb20d6` à la tête du code)", 1),
    ("liste figée `scripts/tests-cibles-iib-v5-v4.txt` (`342ee21d495b54cb5fd4a8ae6d7427043edb3c228cc16afd57ab4f9e3d099b68`, écrite en dur dans l'amorce ; 23 fichiers,",
     "liste figée `scripts/tests-cibles-iib-v5-v5.txt` (`f9ff477d753c675883d81af2dca6721e4c6bc96128b0d17c850eeddca897f1ac`, écrite en dur dans l'amorce ; 24 fichiers,", 1),
    ("**271 essais attendus** : 271 réussis à la tête du code, sur processeur (`sortie-essais-cibles-v5-v5.txt`) ; la liste figée ne change pas, le correctif 0010 ajoute quatre essais à un fichier qu'elle porte déjà (267 avant lui)",
     "**275 essais attendus** : 275 réussis à la tête du code, sur processeur, par la répétition locale du correctif 0012 "
     "(`brouillons/ii-b-saboteur-budget-v5/code-v5/correctif-0012/`) ; le correctif 0011 ajoute le fichier "
     "`tests/test_iib_environnement_machine_v5.py` (quatre essais, qui reproduisent l'environnement de la machine)", 1),
    ("« `271` passed »", "« `275` passed »", 2),
    ("`IIB_TESTS_ATTENDUS=271`", "`IIB_TESTS_ATTENDUS=275`", 1),
]
HISTOIRE = "brouillon 3** : tête locale"   # ligne d'historique de la version 1 : laissée telle quelle
lignes = t.split("\n")
hist = [i for i, l in enumerate(lignes) if HISTOIRE in l]
assert len(hist) == 1
garde = lignes[hist[0]]
lignes[hist[0]] = "@@HISTOIRE@@"
t = "\n".join(lignes)
for ancien, nouveau, n in REMPLACEMENTS:
    assert t.count(ancien) == n, (ancien[:70], t.count(ancien))
    t = t.replace(ancien, nouveau)
t = t.replace("@@HISTOIRE@@", garde)

LIGNE_0010 = "| `correctifs-v5/0010-Organisme-retenu-du-saboteur-budget-code-en-version-.patch` (rang 13) | `d2c339b5b4542c9850edaf2942a8555bdb12da28f9bbb4cfcb06393ac61a7691` |"
assert t.count(LIGNE_0010) == 1
t = t.replace(LIGNE_0010, LIGNE_0010 + "\n"
    "| `correctif-0011/correctifs/0011-Organisme-retenu-du-saboteur-budget-code-en-version-.patch` (rang 14) | `947e5a493929839ef80a1a3f39fa5a4027dd5f430e73496c24c082fd03712ac2` |\n"
    "| `correctif-0012/correctifs/0012-Organisme-retenu-du-saboteur-budget-code-en-version-.patch` (rang 15) | `4cd18c1f2e253935c4d5d3eefb1dc76c40f77006952334cafa2c3ca9c4ad6c73` |")
ORDRE_A = "celles des rangs 9 à 11 sous `brouillons/ii-b-saboteur-budget-v5/code-v5/distillateur-v5/correctifs/`"
assert t.count(ORDRE_A) == 1
t = t.replace(ORDRE_A, ORDRE_A + ", celles des rangs 14 et 15 sous `brouillons/ii-b-saboteur-budget-v5/code-v5/correctif-0011/correctifs/` et "
    "`brouillons/ii-b-saboteur-budget-v5/code-v5/correctif-0012/correctifs/` ; de façon équivalente, les rangs 14 et 15 appliqués sur "
    "`origin/prep/iib-code-v5` (`62356e2ff612a8228b37a8333689e8114099f3c0`, arbre `ed9b0e48be367670cad0782ccb6fbe2d9ca41b87`, les treize premiers rangs déjà appliqués)")

ligne1, reste = t.split("\n", 1)
assert ligne1.startswith("# Ordre — saboteur à budget, organisme retenu (v5) : **étalonnage seul**")
t = ligne1.replace("— brouillon 5", "— version 2, brouillon 1") + "\n\n" + EN_TETE + reste
CIBLE.open("x", encoding="utf-8").write(t)
print(CIBLE.name, hashlib.sha256(t.encode("utf-8")).hexdigest())
