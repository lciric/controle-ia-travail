#!/usr/bin/env python3
"""Essais du contrôle du gel du texte de T0.8 et du programme de scellement (version 2) : cas sains et artefacts (R5).

Usage (depuis la racine du dépôt) : PYTHONPATH=src python3 brouillons/t08-texte-complet-fable-v1/essais-controle-gel-t08-v1.py
Tout se joue dans un dossier temporaire ; rien n'est écrit dans le dépôt ; aucune entropie n'est tirée (les essais qui
écrivent passent `--entropie`). Sortie : une ligne par essai ; code 0 si chaque essai rend l'issue attendue, 1 sinon.
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

ICI = Path("brouillons/t08-texte-complet-fable-v1")
sys.path.insert(0, str(ICI))
import controle_gel_t08_v1 as gel  # noqa: E402

B12 = Path("brouillons/T0.8-bases-boite-noire-v0-v1-brouillon12.md")
FINALISER = ICI / "finaliser-t08-scellement-v2.py"
NEUFS = json.loads((ICI / "textes-neufs-t08-brouillon12-v1.json").read_text(encoding="utf-8"))
VALEURS = NEUFS["valeurs_marqueurs_en_sections_gelees"]
COMMIT = "0123456789abcdef0123456789abcdef01234567"


def une(texte: str, ancien: str, nouveau: str) -> str:
    assert texte.count(ancien) == 1, (texte.count(ancien), ancien[:50])
    return texte.replace(ancien, nouveau)


def artefacts(b12: str) -> dict[str, str]:
    lignes = b12.split("\n")
    i = next(k for k, l in enumerate(lignes) if l.startswith(gel.DEBUT_T5_19))
    t5 = lignes[i]
    j = next(k for k, l in enumerate(lignes) if l.startswith("4. **Graines (R9)**"))
    return {
        "seuil gelé changé (0,10 devient 0,15)": une(b12, "sur la dose ≤ **0,10**", "sur la dose ≤ **0,15**"),
        "phrase gelée de la table F retouchée": une(b12, "« dose intermédiaire : ni diffuse ni flagrante à cette puissance »",
                                                    "« dose moyenne : ni diffuse ni flagrante à cette puissance »"),
        "phrase T5-19 réécrite": une(b12, "**gardée**, option (a), mot de Lazar",
                                     "**gardée**, option (b), et le seuil de « diffuse » est porté à 0,15, mot de Lazar"),
        "phrase T5-19 déplacée": "\n".join(lignes[:i] + lignes[i + 1:j] + [t5] + lignes[j:]),
        "phrase T5-19 doublée": "\n".join(lignes[:i + 1] + [t5] + lignes[i + 1:]),
        "phrase T5-19 retirée": "\n".join(lignes[:i] + lignes[i + 1:]),
        "valeur d'un marqueur altérée (run de 7b)": une(b12, "run `20261111-151701-t06-reel`, branche de sortie",
                                                        "run `20261111-151701-t06-faux`, branche de sortie"),
        "ligne ajoutée dans la liste d'arrêt": une(b12, "\n## Machine, devis et dépense", "\n- Arrêt neuf, non gelé.\n\n## Machine, devis et dépense"),
    }


def ecrire(dossier: Path, nom: str, contenu: str) -> Path:
    p = dossier / nom
    p.write_text(contenu, encoding="utf-8")
    Path(str(p) + ".sha256").write_text(f"{gel.sha(contenu.encode('utf-8'))}  {nom}\n", encoding="utf-8")
    return p


def finaliser(entree: Path, sha_entree: str, rapport: Path, emp: Path, cl: Path, sortie: Path, *plus: str,
              commit: str = COMMIT, depense: str = "essai : engagement, T0.8") -> tuple[int, str]:
    r = subprocess.run([sys.executable, str(FINALISER), "--entree", str(entree), "--sha-entree", sha_entree,
                        "--rapport-verification", str(rapport), "--commit-code", commit, "--empreintes-code", str(emp),
                        "--contre-lecture-code", str(cl), "--ligne-gardes", "R-9999", "--ligne-depense", depense,
                        "--dossier-sortie", str(sortie), *plus], capture_output=True, text=True)
    return r.returncode, (r.stderr or r.stdout).strip().split("\n")[-1][:150]


def main() -> int:
    b12 = B12.read_text(encoding="utf-8")
    sha12 = gel.sha(b12.encode("utf-8"))
    bilan = []

    def noter(nom: str, attendu: str, obtenu: str, detail: str = ""):
        bilan.append(attendu == obtenu)
        print(f"{'conforme' if attendu == obtenu else 'NON CONFORME'} | {nom} | attendu : {attendu} | obtenu : {obtenu} | {detail}")

    # A. le contrôle du gel, appelé directement
    try:
        gel.controler_gel(b12, VALEURS)
        noter("contrôle du gel, brouillon 12 (cas sain)", "tenu", "tenu")
    except SystemExit as e:
        noter("contrôle du gel, brouillon 12 (cas sain)", "tenu", "arrêt", str(e)[:110])
    arts = artefacts(b12)
    for nom, texte in arts.items():
        try:
            gel.controler_gel(texte, VALEURS)
            noter("contrôle du gel, artefact : " + nom, "arrêt", "tenu")
        except SystemExit as e:
            noter("contrôle du gel, artefact : " + nom, "arrêt", "arrêt", str(e)[:90])

    # B. le programme de scellement
    with tempfile.TemporaryDirectory() as d:
        d = Path(d)
        sortie = d / "sortie"
        sortie.mkdir()
        emp = ecrire(d, "empreintes.md", f"commit {COMMIT}\n")
        cl = ecrire(d, "contre-lecture-code.md", "essai\n")
        rapport = ecrire(d, "verification.md", f"brouillon vérifié : {sha12}\n")
        sain = ecrire(d, "sain.md", b12)
        code, msg = finaliser(sain, sha12, rapport, emp, cl, sortie, "--a-blanc")
        noter("scellement à blanc, cas sain", "0", str(code), msg)
        # artefacts du gel, épinglés à leur propre empreinte et à un rapport qui la cite : seul le gel doit les arrêter
        for k, (nom, texte) in enumerate(arts.items()):
            s = gel.sha(texte.encode("utf-8"))
            f = ecrire(d, f"artefact-{k}.md", texte)
            r = ecrire(d, f"verification-{k}.md", f"brouillon vérifié : {s}\n")
            code, msg = finaliser(f, s, r, emp, cl, sortie, "--a-blanc")
            noter("scellement à blanc, artefact : " + nom, "1", str(code), msg)
        # M-8 : une section non gelée modifiée après la vérification
        modifie = une(b12, "Rien n'est lancé, rien n'est dépensé. L'en-tête", "Rien n'est lancé. L'en-tête")
        f = ecrire(d, "non-gele-modifie.md", modifie)
        code, msg = finaliser(f, sha12, rapport, emp, cl, sortie, "--a-blanc")
        noter("scellement à blanc, section non gelée modifiée après la vérification", "1", str(code), msg)
        code, msg = finaliser(f, gel.sha(modifie.encode("utf-8")), rapport, emp, cl, sortie, "--a-blanc")
        noter("scellement à blanc, même fichier, empreinte donnée mais absente du rapport de vérification", "1", str(code), msg)
        # formes
        code, msg = finaliser(sain, sha12, rapport, emp, cl, sortie, "--a-blanc", commit="453a71e1")
        noter("scellement à blanc, commit court", "1", str(code), msg)
        code, msg = finaliser(sain, sha12, rapport, emp, cl, sortie, "--a-blanc", depense="sans la tâche")
        noter("scellement à blanc, ligne de dépense sans la tâche", "1", str(code), msg)
        # écriture réelle dans le dossier temporaire, entropie donnée ; puis rejeu : n'écrase jamais
        code, msg = finaliser(sain, sha12, rapport, emp, cl, sortie, "--entropie", "123456789012345678901234567890")
        noter("scellement réel dans un dossier temporaire, cas sain", "0", str(code), msg)
        ecrit = sortie / "T0.8-bases-boite-noire-v0-v1.md"
        if ecrit.exists():
            t = ecrit.read_text(encoding="utf-8")
            import re
            noter("texte écrit : aucun marqueur restant", "0", str(len(re.findall(r"<<[A-Z0-9_]+>>", t))))
            noter("texte écrit : annexe intacte (phrase « non scellé » du brouillon 10 gardée une fois)", "1",
                  str(t.count("**non scellé** ; il ne vaut pas préenregistrement (R1)")))
            try:
                toutes = dict(VALEURS)
                toutes["ENTROPIE_T08"] = "`123456789012345678901234567890`"
                toutes["LIGNE_MOT_LAZAR_T5_19"] = ("R-2657 (mot de Lazar inscrit le 14 novembre) et R-9999 (gardes de code plus "
                                                   "strictes confirmées ; sort de VT5-07)")
                gel.controler_gel(t, toutes)
                noter("texte écrit : contrôle du gel rejoué", "tenu", "tenu")
            except SystemExit as e:
                noter("texte écrit : contrôle du gel rejoué", "tenu", "arrêt", str(e)[:100])
        code, msg = finaliser(sain, sha12, rapport, emp, cl, sortie, "--entropie", "123456789012345678901234567890")
        noter("scellement réel rejoué sur des sorties existantes", "1", str(code), msg)
    print(f"\n{sum(bilan)} essais conformes sur {len(bilan)}")
    return 0 if all(bilan) else 1


if __name__ == "__main__":
    sys.exit(main())
