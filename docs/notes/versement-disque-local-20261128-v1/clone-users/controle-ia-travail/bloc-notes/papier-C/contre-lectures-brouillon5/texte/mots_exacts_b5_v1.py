"""Contre-lecture texte du brouillon 5 : présence, à l'espace près, des corrections « en mots exacts » des rapports
sur le brouillon 4 (phrases recopiées à la main depuis les rapports ; une ligne par phrase : identifiant <TAB> phrase)."""
import re, sys, pathlib
b5 = re.sub(r"\s+", " ", pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
for ligne in pathlib.Path(sys.argv[2]).read_text(encoding="utf-8").splitlines():
    if not ligne.strip() or ligne.startswith("#"): continue
    ident, phrase = ligne.split("\t", 1)
    p = re.sub(r"\s+", " ", phrase).strip()
    print(("PRÉSENTE " if p in b5 else "ABSENTE  ") + ident + " : " + p[:110])
