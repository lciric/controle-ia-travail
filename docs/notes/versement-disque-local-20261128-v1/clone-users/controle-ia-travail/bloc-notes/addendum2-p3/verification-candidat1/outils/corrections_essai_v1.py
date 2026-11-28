"""Essai des corrections VC1-01 à VC1-05 sur une copie du candidat 1 (addendum 2 de P3) : chaque motif doit être présent
exactement une fois (espaces souples : toute suite de blancs du motif accepte toute suite de blancs du texte) ; écrit
seulement <sortie>, puis imprime `prereg.problemes` et ce que lisent les deux expressions de la garde 1.
L'empreinte du rapport dans l'entrée 6 est fictive ici (2…2). Ce fichier n'est pas un candidat à verser.

Usage (garde R1 active, PYTHONPATH=src) : python -B corrections_essai_v1.py <candidat1> <sortie> <module>
"""
import importlib.util
import re
import sys
from pathlib import Path

from controle_ia.prereg import problemes

src, dst, module = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
t = src.read_text(encoding="utf-8")


def remplace(ancien, nouveau):
    global t
    motif = r"\s+".join(re.escape(x) for x in ancien.split())
    trouves = list(re.finditer(motif, t))
    assert len(trouves) == 1, (len(trouves), ancien[:80])
    t = t[:trouves[0].start()] + nouveau + t[trouves[0].end():]


# VC1-02
remplace("(2026-10-20 vers 21:45 UTC)", "(2026-10-20 vers 21:21 UTC)")
# VC1-04, 1
remplace("les trois tests proposés et éprouvés par la lentille « code » (VV3-code-01 à 03), ajoutés sans changement "
         "(128 tests)",
         "les trois fonctions de test proposées et éprouvées par la lentille « code » (VV3-code-01 à 03), ajoutées sans "
         "changement (7 tests de plus, 128 en tout)")
# VC1-01, 1
remplace("script `…/addendum2-p3/candidat/ecrire_candidat1_addendum2_v1.py`",
         "script `prereg/contre-lectures/brouillons-addendum2-P3-v1/ecrire_candidat1_addendum2_v1.py` (sha256 "
         "`94560a3b690facfc8a68a39d34f069afba44771156387f7978fcdc7877078593`), qui écrit tout le candidat 1 sauf cette "
         "ligne, ajoutée ensuite")
# VC1-04, 2
remplace("(30 mutants neufs sur les points changés, 24 tués, 2 équivalents ; trois tests proposés). Tests v4 : les 121 "
         "tests relus et les trois tests proposés et éprouvés par la lentille « code » (VV3-code-01 à 03), ajoutés sans "
         "changement, soit 128 tests",
         "(30 mutants neufs sur les points changés : 24 tués, 6 survivants dont 2 équivalents ; les 4 autres, VV-G6-02, "
         "VV-F-01, VV-F-02 et VV-D3-04, sont tués par les trois fonctions de test proposées). Tests v4 : les 121 tests "
         "relus et les trois fonctions de test proposées et éprouvées par la lentille « code » (VV3-code-01 à 03), "
         "ajoutées sans changement, soit 7 tests de plus (le test de la garde 7 compte une fois par forme) et 128 tests")
# VC1-03, 1
remplace("passés sous la garde R1 (0 refus).",
         "passés sous la garde R1 (128 passés, 0 refus ; journaux "
         "`prereg/contre-lectures/tests-v4-addendum2-P3-v1/pytest-suite-v4-garde-r1.log`, sha256 "
         "`cb24c899aa490bfa98e00b370c0ad388f13ddfbce6f277b21bd368a24ba12c36`, et "
         "`prereg/contre-lectures/tests-v4-addendum2-P3-v1/r1-suite-v4.jsonl`, sha256 "
         "`f2a4be52af0304831d77abeb36d78c46bb073f1a606f7eb56e3b0e3f576b3edd`).")
# VC1-05
remplace("Constats traités dans le texte (ce candidat) ; le module relu est le module cité en tête.",
         "Constats traités : VV3-texte-01 à 07 et VV3-code-05 dans le texte (ce candidat) ; VV3-code-01 à 03 par les "
         "trois fonctions de test ; VV3-code-04 par les mots de VV3-texte-02 (précision 14), sans le test facultatif ; "
         "VV3-code-01, point 3 (notes) : notes v3 laissées telles quelles, G6-02 étant désormais tué par "
         "`test_garde_6_au_lancement_exception_du_chargeur_convertie` ; le module relu est le module cité en tête.")
# VC1-03, 2 (recommandé) : entrée 6, à la fin de la section « Contre-lecture » (fin du fichier)
assert t.endswith("le module relu est le module cité en tête.\n")
t += ("- **Contre-lecture 6** — vérification mécanique du candidat 1 (sha256 "
      "`9900a721560c87361efcf60660863727644e8fdc3ab88e4fd1f325a613306b0e`) et des tests v4 (sha256 "
      "`f9136b6dc5eebce6d9e9101fa910646b16fa544f0ee1d3a997030eb9319dbc07`) par un sous-agent neuf, qui n'a écrit ni le "
      "texte, ni aucune version du module ou de ses tests, ni aucune contre-lecture antérieure : rapport "
      "`prereg/contre-lectures/verification-candidat1-addendum2-P3-v1.md` (sha256 `" + "2" * 64 + "`), « scellable après "
      "corrections » ; suite v4 relancée sous la garde R1 (128 passés, 0 refus) ; chaque test ajouté tue le mutant qu'il "
      "vise. Constats VC1-01 à VC1-05 traités dans ce candidat.\n")

dst.write_text(t, encoding="utf-8")
print("problemes :", problemes(dst))
spec = importlib.util.spec_from_file_location("av_essai_vc1", module)
av = importlib.util.module_from_spec(spec)
spec.loader.exec_module(av)
print("garde 1, module :", av.EMPREINTE_MODULE_CITEE.findall(t))
print("garde 1, tests  :", av.EMPREINTE_TESTS_CITEE.findall(t))
