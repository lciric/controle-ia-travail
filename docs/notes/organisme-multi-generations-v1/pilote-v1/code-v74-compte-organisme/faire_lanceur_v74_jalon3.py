"""Jalon 3 du lanceur v74 (contre-lecture du code v74, constats 1a, 5 et 6) : appliqué sur la sortie de `faire_lanceur_v74.py`,
remplacements comptés : dossier de l'appel calculé une fois ; garde : total d'usage ≠ entrée + sortie arrête aussi le pilote ;
manifeste : la liste des proposeurs « sans réflexion »."""
import sys
p = sys.argv[1] + "/demonstrations/pilote_mr2_v74.py"
t = open(p, encoding="utf-8").read()
R = [
 ('                r = PR.appeler(conf, nom, s["texte"], os.path.join(args.sortie, f"monde-{w}", nom), jeton, python=sys.executable)\n'
  '                garder_reflexion_absente(conf, nom, os.path.join(args.sortie, f"monde-{w}", nom), r, sans_reflexion)',
  '                dossier_appel = os.path.join(args.sortie, f"monde-{w}", nom)  # v74 : un seul chemin, pour l\'appel et pour la garde\n'
  '                r = PR.appeler(conf, nom, s["texte"], dossier_appel, jeton, python=sys.executable)\n'
  '                garder_reflexion_absente(conf, nom, dossier_appel, r, sans_reflexion)'),
 ('''        raise PR.ArretPilote(f"{nom} : champ de réflexion apparu en cours de course (réflexion comptée {t!r}) alors que la sonde "
                             f"l'a dit absent : arrêt du pilote (v74)", appel=r)
''', '''        raise PR.ArretPilote(f"{nom} : champ de réflexion apparu en cours de course (réflexion comptée {t!r}) alors que la sonde "
                             f"l'a dit absent : arrêt du pilote (v74)", appel=r)
    if d == "gemini" and isinstance(u, dict) and "totalTokenCount" in u and not S.sans_effet_d_un_appel(u):
        raise PR.ArretPilote(f"{nom} : total d'usage ≠ entrée + sortie (jetons cachés possibles) alors que la sonde a dit aucune "
                             f"réflexion cachée : arrêt du pilote (v74)", appel=r)
'''),
 ('                 "releve_sonde_sha256": releve_sha,\n', '                 "releve_sonde_sha256": releve_sha, "proposeurs_sans_reflexion": sans_reflexion,  # v74\n'),
 ("    arrête le pilote (code 3, l'appel porté au relevé partiel avec sa dépense) si un champ de réflexion apparaît dans l'usage brut\n    de son appel (corps du relais), ou si la commande lui compte une réflexion non nulle.",
  "    arrête le pilote (code 3, l'appel porté au relevé partiel avec sa dépense) si un champ de réflexion apparaît dans l'usage brut\n    de son appel (corps du relais), si la commande lui compte une réflexion non nulle, ou (Argon) si son total d'usage n'est pas\n    entrée + sortie (jetons cachés possibles)."),
]
for a, b in R:
    assert t.count(a) == 1, (a[:80], t.count(a))
    t = t.replace(a, b)
open(p, "w", encoding="utf-8").write(t)
print("jalon 3 appliqué")
