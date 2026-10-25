"""Applique la correction candidate C-12 à principal.py de la v5 de Gemini (remplacements exacts, chacun unique).
Usage : python -I appliquer_c12_v1.py CHEMIN_PRINCIPAL"""
import pathlib, sys
p = pathlib.Path(sys.argv[1])
t = p.read_text(encoding="utf-8")
remplacements = [
    ('            compteurs["recherches_echec"] = compteurs.get("recherches_echec", 0) + 1\n'
     '            _consigner_erreur(f"recherche #{num} ({source}) non OK : statut={statut}")\n',
     '            compteurs["recherches_echec"] = compteurs.get("recherches_echec", 0) + 1\n'),
    ('            "echec": rep.get("echec"),\n        })\n    return {"ok": est_ok, "statut": statut, "resultats": resultats, "brut": rep}\n',
     '            "echec": rep.get("echec"),\n        })\n'
     '    if not est_ok:  # C-12 : consigné hors du verrou (_VERROU n\'est pas réentrant et _consigner_erreur le prend)\n'
     '        _consigner_erreur(f"recherche #{num} ({source}) non OK : statut={statut}")\n'
     '    return {"ok": est_ok, "statut": statut, "resultats": resultats, "brut": rep}\n'),
    ('            compteurs["telechargements_echec"] = compteurs.get("telechargements_echec", 0) + 1\n'
     '            _consigner_erreur(f"téléchargement #{num} ({ref_propre[:60]}) non OK : statut={statut}")\n',
     '            compteurs["telechargements_echec"] = compteurs.get("telechargements_echec", 0) + 1\n'),
    ('            "echec": rep.get("echec"),\n        })\n    return {\n        "ok": est_ok,\n',
     '            "echec": rep.get("echec"),\n        })\n'
     '    if not est_ok:  # C-12 : consigné hors du verrou (_VERROU n\'est pas réentrant et _consigner_erreur le prend)\n'
     '        _consigner_erreur(f"téléchargement #{num} ({ref_propre[:60]}) non OK : statut={statut}")\n'
     '    return {\n        "ok": est_ok,\n'),
]
for ancien, nouveau in remplacements:
    n = t.count(ancien)
    if n != 1:
        sys.exit(f"refus : motif trouvé {n} fois (attendu 1) : {ancien[:70]!r}")
    t = t.replace(ancien, nouveau)
p.write_text(t, encoding="utf-8", newline="\n")
print("C-12 appliquée :", len(remplacements), "remplacements")
