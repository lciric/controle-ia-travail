"""Simulation (vérificateur neuf) : les phrases à reporter au texte, appliquées par paires exactes au candidat 1.

But : montrer que chaque ancre se trouve une seule fois, que la table « Critères de lecture gelés » n'est pas touchée
(la garde du module v2 passe encore) et que le validateur `controle_ia.prereg.problemes` ne trouve rien. Le résultat
est une SIMULATION, pas un candidat : il n'est pas scellé et ne doit servir à rien d'autre.

Usage (depuis la racine du dépôt) :
  PYTHONPATH=src:<module-v2> python -B simuler_phrases_v1.py <candidat1.md> <module-v2> <sortie simulation .md>
"""
import hashlib
import json
import sys
from pathlib import Path

import lecture_p4_v1 as lp
from controle_ia.prereg import problemes

DOSSIER = "docs/procedures/P4-instrument-v1"
ANCIENNES = {
    "mesures_conception_p4_v1.py": "483b8ac3aca65a9879b7d2f2a832cfd5478c48fd860c94a6fbdc041364cc8be7",
    "instrument_p4_v1.py": "6e0e026eafba28e708fea009cc5c81c8b95defe6aa8f9fc2f76dd364ee29b06c",
    "lecture_p4_v1.py": "51a25e30a70b2439046e87037d6e2fcb26616289a017ef10689d66c0ca50e213",
    "test_instrument_p4_v1.py": "9d015be4ce2bbff4a4541387d5d19ef70497aa41f1a53b9c38724360d7a1dffd",
    "test_lecture_p4_v1.py": "49441971b81a89fe4b0dcc392efa7eba81234972d1d8e60abd4cececa33111d9",
    "test_gardes_p4_v1.py": "f4f97029f9a1fb9d9d1b29bac162334305a001b091319fde250e188071e092f5",
}

PAIRES = [
    # T2 de la chaîne (forme lue par la chaîne), comme `ecrire_candidat2_v1.py` l. 116, avec 1123
    ("- Tests attendus : 1 102, soit", "- Tests attendus : `1123`, soit", "T2 (forme de la chaîne), N = 908 + 215"),
    # phrase 4 du correcteur, réduite au reste de la ligne (VM2-fidelite-02)
    ("les 194 du module de P4 (71, 42 et 81 ; chaque fichier\n  écrit son nombre et le vérifie).",
     "les 215 du module de P4 (71, 43 et 101 ; chaque fichier\n  écrit son nombre et le vérifie ; la suite du module se "
     "lance avec `P4_TEXTE_PREREG=prereg/P4-instrument-v1.md`, sans\n  quoi le test qui compare la table du module à "
     "celle de ce texte échoue).", "phrase 4 (reste de la ligne)"),
    # phrases 1 et 2 du correcteur (liste d'arrêt)
    ("- Lecture demandée avant le scellement du verdict complété de P3 (addendum 2), ou avant le scellement de ce texte :\n"
     "  refusée sans rien écrire et reportée (pas une ligne).",
     "- Lecture demandée avant le scellement du verdict complété de P3 (addendum 2), ou avant le scellement de ce texte,\n"
     "  ou sans `--prereg` sur un run source décisif ou en mode réel : refusée sans rien écrire et reportée (pas une ligne).\n"
     "- Lecture décisive dont la table « Critères de lecture gelés » de ce texte diffère de la table du module (`LIGNES`\n"
     "  de `lecture_p4_v1.py`) d'une cellule, d'une ligne ou de l'ordre : refusée sans rien écrire (pas une ligne) ; écart\n"
     "  entre le texte et le module : nœud.", "phrases 1 et 2"),
    # phrase 3 du correcteur (Tests (R5)), ancre avec son retour à la ligne
    ("C1 au pas 0 et Δ net\n  recalculés à la main sur un jeu synthétique.",
     "C1 au pas 0 et Δ net\n  recalculés à la main sur un jeu synthétique ; lecture sans `--prereg` d'un run décisif ou en "
     "mode réel (doit refuser\n  sans rien écrire), contre un run jouet non décisif (doit lire) ; table « Critères de "
     "lecture gelés » de ce texte\n  différente d'une cellule de la table du module (doit refuser sans rien écrire), et "
     "table du module égale à celle de\n  ce texte, cellule par cellule (test lancé avec `P4_TEXTE_PREREG`, qui échoue "
     "sans elle).", "phrase 3"),
    # VM2-fidelite-03 : plan d'analyse, point 2 (CR-07 rendu obligatoire, plus la lecture sans --prereg)
    ("module à l'empreinte\n   citée (`exiger_module_cite`) ;",
     "module à l'empreinte\n   citée (`exiger_module_cite`) ; table « Critères de lecture gelés » de ce texte égale à "
     "celle du module, cellule par\n   cellule (sinon refus, rien n'est écrit, pas une ligne) ;", "VM2-fidelite-03 (a)"),
    ("sans autre table\n   (VP3-06).",
     "sans autre table\n   (VP3-06). Sans `--prereg`, seul un run source ni décisif ni en mode réel se lit (répétition "
     "jouet) ; un run\n   source décisif ou en mode réel est refusé sans rien écrire (liste d'arrêt).",
     "VM2-fidelite-03 (b)"),
    # VM2-fidelite-04 : chaîne de lancement, nombre de tests
    ("(faits, 194 tests)", "(faits, 194 tests ; module v2 après la contre-lecture 3 : 215 tests)", "VM2-fidelite-04"),
]


def main(argv):
    cand1, module_dir, sortie = Path(argv[0]), Path(argv[1]), Path(argv[2])
    t = cand1.read_text(encoding="utf-8")
    journal = []
    for n, ancienne in ANCIENNES.items():
        neuve = hashlib.sha256((module_dir / n).read_bytes()).hexdigest()
        a = f"Module de P4 : `{DOSSIER}/{n}` : `{ancienne}`"
        journal.append({"paire": f"module {n}", "trouvee": t.count(a)})
        assert t.count(a) == 1
        t = t.replace(a, f"Module de P4 : `{DOSSIER}/{n}` : `{neuve}`")
    for a, b, s in PAIRES:
        journal.append({"paire": s, "trouvee": t.count(a)})
        assert t.count(a) == 1, s
        t = t.replace(a, b)
    sortie.write_text(t, encoding="utf-8")
    garde = lp.exiger_table_des_criteres(t)
    print(json.dumps({"paires": journal, "garde_table": garde, "problemes_validateur": problemes(sortie),
                      "tests_attendus_lus_comme_la_chaine": __import__("re").findall(r"Tests attendus : `([0-9][0-9]*)`", t),
                      "sha256_simulation": hashlib.sha256(t.encode("utf-8")).hexdigest()}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main(sys.argv[1:])
