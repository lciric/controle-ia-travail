"""Épreuves du contrôle des citations de la v2 sur un cas sain et sur des artefacts (R5) — v1.

Fabrique des copies altérées de la note v2 (chaque remplacement doit se trouver exactement une fois dans la note,
sinon arrêt), lance le contrôleur sur la note puis sur chaque copie, et exige : code 0 pour la note ; code 1 pour
chaque copie, avec un refus qui porte sur la citation visée (attendu de la ligne de refus). Écrit le journal.
Usage : python3 -B -I epreuves_v2_v1.py CONTROLEUR NOTE_V2 NOTE_V1 DOSSIER_ARTEFACTS JOURNAL PDF_LU ID=PDF ...
"""
import difflib
import hashlib
import os
import subprocess
import sys

ARTEFACTS = [
    ("a1-mot-change-citation-neuve-v1.md",
     "“though nothing was retuned on held-out data” (p. 9)",
     "“though nothing was retrained on held-out data” (p. 9)",
     ("ECHEC", "retrained")),
    ("a2-mauvaise-page-citation-neuve-v1.md",
     "elle “does not adjust for turn position in neutral-reply conversations” (p. 9)",
     "elle “does not adjust for turn position in neutral-reply conversations” (p. 8)",
     ("ECHEC", "LU p. 8 ; aussi lue en [9]")),
    ("a3-couche-cachee-tableau-v1.md",
     "Toute extraction automatique de la p. 7 doit l'écarter (section 6).",
     "Toute extraction automatique de la p. 7 doit l'écarter (section 6). Épreuve : “Pre-registered misbehaviour comparisons” (p. 7).",
     ("COUCHE", "Pre-registered misbehaviour comparisons")),
    ("a3b-couche-cachee-limites-v1.md",
     "Toute extraction automatique de la p. 7 doit l'écarter (section 6).",
     "Toute extraction automatique de la p. 7 doit l'écarter (section 6). Épreuve : “Every result comes from one model” (p. 7).",
     ("COUCHE", "Every result comes from one model")),
    ("a4-sans-page-v1.md",
     "Toute extraction automatique de la p. 7 doit l'écarter (section 6).",
     "Toute extraction automatique de la p. 7 doit l'écarter (section 6). Épreuve : “These results are preliminary” sans renvoi.",
     ("SANS-PAGE", "These results are preliminary")),
    ("a5-autre-source-change-v1.md",
     "“The direction fires in these conversations (Section 4.1)” (2609.16247v2, p. 21)",
     "“The direction fires in these conversations (Section 4.2)” (2609.16247v2, p. 21)",
     ("ECHEC", "Section 4.2")),
    ("a6-source-inconnue-v1.md",
     "“The direction fires in these conversations (Section 4.1)” (2609.16247v2, p. 21)",
     "“The direction fires in these conversations (Section 4.1)” (2609.16248v2, p. 21)",
     ("SOURCE?", "2609.16248v2")),
]


def sha(chemin):
    return hashlib.sha256(open(chemin, "rb").read()).hexdigest()


def lancer(controleur, note, ref, pdfs):
    r = subprocess.run([sys.executable, "-B", "-I", controleur, note, pdfs[0], "--reference", ref, *pdfs[1:]],
                       capture_output=True, text=True, env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
    return r.returncode, r.stdout


def main(argv):
    controleur, note, ref, dossier, journal = argv[1:6]
    pdfs = argv[6:]
    texte = open(note, encoding="utf-8").read()
    lignes = [f"# Journal des épreuves du contrôle des citations — note v2 — v1",
              f"contrôleur {sha(controleur)}  {os.path.basename(controleur)}",
              f"note v2    {sha(note)}  {os.path.basename(note)}",
              f"note v1    {sha(ref)}  {os.path.basename(ref)}", ""]
    echecs = 0
    code, sortie = lancer(controleur, note, ref, pdfs)
    bilan = sortie.strip().splitlines()[-1]
    ok = code == 0
    echecs += not ok
    lignes += ["## Cas sain : la note v2 (attendu : code 0)", f"code {code} ; {bilan} ; {'CONFORME' if ok else 'NON CONFORME'}", ""]
    os.makedirs(dossier, exist_ok=True)
    for nom, avant, apres, (etat, motif) in ARTEFACTS:
        if texte.count(avant) != 1:
            raise SystemExit(f"{nom} : le passage à remplacer apparaît {texte.count(avant)} fois (1 attendu)")
        altere = texte.replace(avant, apres)
        chemin = os.path.join(dossier, nom)
        if os.path.exists(chemin):
            raise SystemExit(f"{chemin} existe déjà : on n'écrase jamais (R12)")
        open(chemin, "w", encoding="utf-8").write(altere)
        code, sortie = lancer(controleur, chemin, ref, pdfs)
        refus = [l for l in sortie.splitlines() if not l.startswith("OK") and not l.startswith("BILAN")]
        vise = [l for l in refus if l.startswith(etat) and motif in l]
        ok = code == 1 and len(refus) == 1 and len(vise) == 1
        echecs += not ok
        ecart = [l for l in difflib.unified_diff(texte.splitlines(), altere.splitlines(), lineterm="", n=0)
                 if l[:1] in "+-" and not l.startswith(("+++", "---"))]
        lignes += [f"## Artefact {nom} (attendu : code 1, refus « {etat} » visant « {motif} »)",
                   f"{sha(chemin)}  {nom}", f"écart à la note : {len(ecart) // 2} ligne(s)"]
        lignes += [f"    {l}" for l in refus] + [f"code {code} ; {'CONFORME' if ok else 'NON CONFORME'}", ""]
    lignes.append(f"BILAN DES ÉPREUVES : {1 + len(ARTEFACTS)} cas, {echecs} non conforme(s)")
    open(journal, "w", encoding="utf-8").write("\n".join(lignes) + "\n")
    print("\n".join(lignes))
    return 1 if echecs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
