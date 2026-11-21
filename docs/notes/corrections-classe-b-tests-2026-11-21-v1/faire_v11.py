"""Fabrique scripts/lancer_course_auto_conception_v11.py à partir de la v10, par substitutions nommées (chacune doit
s'appliquer exactement une fois). Usage : python3 -I faire_v11.py RACINE_DE_LA_COPIE"""
import sys
from pathlib import Path

racine = Path(sys.argv[1])
src = (racine / "scripts/lancer_course_auto_conception_v10.py").read_text(encoding="utf-8")

ENTETE_V11 = '''"""Lanceur de la course d'auto-conception de l'organisme d'idéation — version 11 (correction du filtre « programme à
épingler » : l'interpréteur qui joue le lanceur n'est plus compté comme programme).

Version 11 (R12 ; la v10, `scripts/lancer_course_auto_conception_v10.py`, `f4196ec5…a07a`, reste en place). Lot de corrections
de classe B des essais complets du 21 novembre 2026 (tri `registres/essaim/vers-mere/annexe-tests-complets-2026-11-21-v1/
tri-echecs-tests-complets-2026-11-21-v1.md`, `9957b178…`, § 1). Ce que la v11 change, et rien d'autre :
1. **filtre des programmes à épingler** (`verifier_declaration`, commandes d'Astra et de Carbon) : en plus des fichiers sous
   `/usr/` et `/bin/`, sont écartés `sys.executable` et sa cible résolue (`os.path.realpath`). Sous l'environnement virtuel
   prescrit (`.venv/bin/python`, lien hors de `/usr/`), l'interpréteur n'est plus compté comme programme non épinglé ; tout
   autre fichier de la commande hors de `/usr/` et `/bin/` reste à épingler, comme en v10 ;
2. noms propres à la version : `VERSION`, dossier de sortie, suffixe des runs, la v10 comptée parmi les versions déjà lancées
   (suffixes et dossiers de sortie), en-tête du registre dérivé, dossier d'alerte de crédit, et le message du refus « tentative
   déjà lancée ».
Le reste est la v10, y compris les interrupteurs (éteints par défaut, bloc `interrupteurs_v10`, `BLOCAGES_REELS_V10`) : la v11
**ne lève aucun des blocages du moteur réel allumé** que la v10 renvoie à un « lanceur v11 » ; ce nom est pris ici par la seule
correction du filtre. Cette version n'a ni contre-lecture ni pièce de départ qui l'épingle : elle ne part pas en réel en l'état.

Texte de la v10 :

Lanceur de la course d'auto-conception de l'organisme d'idéation — version 10'''

SUBS = [
    ('"""Lanceur de la course d\'auto-conception de l\'organisme d\'idéation — version 10', ENTETE_V11, "en-tête v11"),
    ('VERSION = "lancer_course_auto_conception_v10"', 'VERSION = "lancer_course_auto_conception_v11"', "VERSION"),
    ('DOSSIER_SORTIES = Path("/home/user/sorties-course-auto-conception-v10")     # v10 : dossier de sortie neuf (nom de version)',
     'DOSSIER_SORTIES = Path("/home/user/sorties-course-auto-conception-v11")     # v11 : dossier de sortie neuf (nom de version)',
     "DOSSIER_SORTIES"),
    ('SUFFIXE_RUN = "-course-auto-conception-v10"', 'SUFFIXE_RUN = "-course-auto-conception-v11"', "SUFFIXE_RUN"),
    ('''                        "-course-auto-conception-v7", "-course-auto-conception-v8", "-course-auto-conception-v9",
                        SUFFIXE_RUN)                                  # v10 : la v9 comptée parmi les versions déjà lancées''',
     '''                        "-course-auto-conception-v7", "-course-auto-conception-v8", "-course-auto-conception-v9",
                        "-course-auto-conception-v10",
                        SUFFIXE_RUN)                                  # v11 : la v10 comptée parmi les versions déjà lancées''',
     "SUFFIXES_DEJA_LANCEE"),
    ('''                           Path("/home/user/sorties-course-auto-conception-v9"))''',
     '''                           Path("/home/user/sorties-course-auto-conception-v9"), Path("/home/user/sorties-course-auto-conception-v10"))''',
     "SORTIES_AUTRES_VERSIONS"),
    ('raise Refus(f"tentative v10 déjà lancée', 'raise Refus(f"tentative v11 déjà lancée', "message tentative"),
    ("(course d'auto-conception, lanceur v10) — lignes nommées seulement",
     "(course d'auto-conception, lanceur v11) — lignes nommées seulement", "en-tête du registre dérivé"),
    ('"-alerte-credits-auto-conception-v10"', '"-alerte-credits-auto-conception-v11"', "dossier d'alerte de crédit"),
    ('''            fichiers = [x for x in b["commande"] if isinstance(x, str) and os.path.isfile(x) and not x.startswith(("/usr/", "/bin/"))]''',
     '''            interpretes = {sys.executable, os.path.realpath(sys.executable)}  # v11 : l'interpréteur qui joue le lanceur, et sa cible
            fichiers = [x for x in b["commande"] if isinstance(x, str) and os.path.isfile(x) and not x.startswith(("/usr/", "/bin/"))
                        and x not in interpretes]''',
     "filtre"),
]

for vieux, neuf, motif in SUBS:
    n = src.count(vieux)
    if n != 1:
        raise SystemExit(f"{motif} : {n} occurrence(s), 1 exigée")
    src = src.replace(vieux, neuf)

(racine / "scripts/lancer_course_auto_conception_v11.py").write_text(src, encoding="utf-8")
print("écrit")
