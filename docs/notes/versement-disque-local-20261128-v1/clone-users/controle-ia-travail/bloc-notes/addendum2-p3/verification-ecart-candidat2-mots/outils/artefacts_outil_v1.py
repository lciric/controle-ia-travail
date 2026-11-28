"""Épreuve de l'outil mots_exacts_ecart_v1.py (R5) : il doit dire « True » sur le candidat 2 sain et « False » (ou
« CHANGE ») sur des artefacts construits depuis le candidat 2.

Usage : python -I -B artefacts_outil_v1.py OUTIL RAPPORT CANDIDAT1 CANDIDAT2 LIGNE SCRIPT DOSSIER
"""
import subprocess
import sys
from pathlib import Path


def seuil_change(t):
    i = t.index("\n## Seuil")
    j = next(k for k in range(i, len(t)) if t[k].isdigit())
    return t[:j] + str((int(t[j]) + 1) % 10) + t[j + 1:]


def main(argv):
    outil, rapport, c1, c2, ligne, script, dossier = argv[1:8]
    t = Path(c2).read_text(encoding="utf-8")
    artefacts = {
        "sain (candidat 2 tel quel)": t,
        "a. un mot changé dans l'entrée 6 (« un sous-agent neuf » -> « un sous-agent »)":
            t.replace("par un sous-agent neuf, qui n'a écrit ni le\n  texte, ni aucune version",
                      "par un sous-agent, qui n'a écrit ni le\n  texte, ni aucune version"),
        "b. un chiffre changé dans « Seuil » (premier chiffre de la section, +1 modulo 10), hors corrections":
            seuil_change(t),
        "c. VC1-05 non appliqué (ancien texte remis)":
            t.replace("Constats traités : VV3-texte-01 à 07 et\n  VV3-code-05 dans le texte (ce candidat) ; VV3-code-01 à 03 par "
                      "les trois fonctions de test ; VV3-code-04 par les\n  mots de VV3-texte-02 (précision 14), sans le test "
                      "facultatif ; VV3-code-01, point 3 (notes) : notes v3 laissées\n  telles quelles, G6-02 étant désormais "
                      "tué par `test_garde_6_au_lancement_exception_du_chargeur_convertie` ; le\n  module relu est le module "
                      "cité en tête.",
                      "Constats traités dans le texte\n  (ce candidat) ; le module relu est le module cité en tête."),
        "d. seulement un retour à la ligne déplacé dans l'entrée 6 (doit rester vrai, espaces normalisés)":
            t.replace("Constats VC1-01 à\n  VC1-05 traités", "Constats\n  VC1-01 à VC1-05 traités"),
        "e. chevron de l'entrée 6 rempli par une autre empreinte":
            t.replace("3f0dce9ba99ab692b2d47660457a28b969ac3b0ac04b43f931f0101f05283f04",
                      "3f0dce9ba99ab692b2d47660457a28b969ac3b0ac04b43f931f0101f05283f05"),
    }
    for nom, txt in artefacts.items():
        changed = txt != t
        p = Path(dossier) / "artefact.md"
        p.write_text(txt, encoding="utf-8")
        r = subprocess.run([sys.executable, "-I", "-B", outil, rapport, c1, str(p), ligne, script],
                           capture_output=True, text=True)
        lignes = [x.strip() for x in r.stdout.splitlines()
                  if "candidat 2 normalisé =" in x or "CHANGE" in x or "entrée 6 (normalisée)" in x]
        print(f"== {nom} ; artefact différent du candidat 2 : {changed or nom.startswith('sain')} ; code {r.returncode}")
        for x in lignes:
            print("   " + x)
        p.unlink()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
