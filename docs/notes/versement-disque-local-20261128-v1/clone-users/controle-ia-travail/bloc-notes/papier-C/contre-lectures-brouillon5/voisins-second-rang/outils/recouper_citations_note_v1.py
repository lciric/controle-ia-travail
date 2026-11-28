"""Recoupe toutes les citations entre guillemets français de la note avec les sources.
Pour chaque citation « … » de la note, cherche le texte (normalisé comme dans
verifier_citations_second_rang_v1.py) dans toutes les pages de tous les documents.
Affiche les citations introuvables, à examiner une à une (les phrases françaises de la note
en font partie et sont attendues). Usage : python3 -I -B recouper_citations_note_v1.py RACINE NOTE
"""
import importlib.util
import os
import re
import sys

racine, note = sys.argv[1], sys.argv[2]
spec = importlib.util.spec_from_file_location(
    "verif", os.path.join(racine, "outils", "verifier_citations_second_rang_v1.py"))
sys.argv = [sys.argv[0], racine, "--sans-controle"]
verif = importlib.util.module_from_spec(spec)
# Le module lance son contrôle au chargement ; on capte sa sortie et on ignore son code de retour.
import contextlib, io
tampon = io.StringIO()
try:
    with contextlib.redirect_stdout(tampon):
        spec.loader.exec_module(verif)
except SystemExit:
    pass

texte = open(note, encoding="utf-8").read()
citations = re.findall(r"«\s*(.*?)\s*»", texte, re.S)
introuvables = 0
for c in citations:
    c1 = re.sub(r"\s+", " ", c).strip()
    if len(c1) < 12:
        continue
    cible = verif.variantes(c1)[0]
    trouve = False
    for doc, (genre, chemin, _) in verif.DOCS.items():
        pages = verif.pages_pdf(chemin) if genre == "pdf" else verif.blocs_html(chemin)
        if any(cible in v for vs in pages.values() for v in vs):
            trouve = True
            break
    if not trouve:
        introuvables += 1
        print("INTROUVABLE :", c1[:150])
print(f"{len(citations)} citations dans la note ; {introuvables} introuvables (à examiner)")
