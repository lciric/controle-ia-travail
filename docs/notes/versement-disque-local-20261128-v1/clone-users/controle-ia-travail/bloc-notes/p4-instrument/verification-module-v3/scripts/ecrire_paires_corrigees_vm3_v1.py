"""Paires du texte corrigees par la verification du module v3 (VM3-01) : memes ancres que
`module-v3-travail/paires-texte-module-v3-v3.json` ; seuls les « nouveau » des paires 1, 4 et 5 changent. Ecrit le JSON
(liste de {"source", "ancien", "nouveau"}) et imprime, pour chaque ligne neuve, sa longueur.

Usage : python -B ecrire_paires_corrigees_vm3_v1.py PAIRES_V3 SORTIE_JSON
"""
from __future__ import annotations

import sys

sys.dont_write_bytecode = True

import json  # noqa: E402
from pathlib import Path  # noqa: E402

entree, sortie = Path(sys.argv[1]), Path(sys.argv[2])
paires = json.loads(entree.read_text(encoding="utf-8"))
assert len(paires) == 7

ANCIEN_TIRET_3 = ("- Manifeste lu sous `runs/<run source>/`, résumé ou identité du run source dont l'identifiant de run n'est pas\n"
                  "  celui du dossier (copie, lien symbolique, chemin détourné) : lecture refusée sans rien écrire (pas une ligne).")
NOUVEAU_TIRET_3 = ("- Manifeste lu sous `runs/<run source>/`, résumé ou identité du run source dont l'identifiant de run n'est pas\n"
                   "  celui du dossier (copie, lien symbolique, chemin détourné), vu au chargement des données du run : lecture\n"
                   "  refusée sans rien écrire (pas une ligne) ; en mode décisif, une autre garde du mode décisif qui refuse avant ce\n"
                   "  chargement écrit L1 (plan d'analyse, point 2).")
ANCIEN_TIRET_2 = ("  de `lecture_p4_v1.py`) d'une cellule, d'une rangée ou de l'ordre ; section « Critères de lecture gelés » présente\n"
                  "  plus d'une fois ; rangée, entre l'en-tête et la fin du tableau, hors de la forme `| Lk | issue | lecture |` :\n"
                  "  refusée sans rien écrire (pas une ligne) ; écart entre le texte et le module : nœud.")
NOUVEAU_TIRET_2 = ("  de `lecture_p4_v1.py`) d'une cellule, d'une rangée ou de l'ordre ; section « Critères de lecture gelés » présente\n"
                   "  plus d'une fois, ou dont une autre ligne que celles du tableau porte une barre (seconde table) ; rangée, entre\n"
                   "  l'en-tête et la fin du tableau, hors de la forme `| Lk | issue | lecture |` : refusée sans rien écrire (pas une\n"
                   "  ligne) ; écart entre le texte et le module : nœud.")

p1 = paires[0]
assert p1["nouveau"].count(ANCIEN_TIRET_3) == 1 and p1["nouveau"].count(ANCIEN_TIRET_2) == 1
p1["nouveau"] = p1["nouveau"].replace(ANCIEN_TIRET_3, NOUVEAU_TIRET_3).replace(ANCIEN_TIRET_2, NOUVEAU_TIRET_2)
p1["source"] += " ; corrigée par la vérification du module v3 (VM3-01)"

p4 = paires[3]
assert p4["ancien"] == "module à l'empreinte\n   citée (`exiger_module_cite`) ;"
p4["nouveau"] = ("module à l'empreinte\n"
                 "   citée (`exiger_module_cite`) ; table « Critères de lecture gelés » de ce texte égale à celle du module, lue en\n"
                 "   entier : section présente une seule fois, sans autre ligne à barre que celles du tableau ; chaque rangée, entre\n"
                 "   l'en-tête et la fin du tableau, de la forme « `| Lk | issue | lecture |` » ; mêmes rangées, même ordre, mêmes\n"
                 "   cellules (sinon refus, rien n'est écrit, pas une ligne) ;")
p4["source"] += " ; corrigée par la vérification du module v3 (VM3-01)"

p5 = paires[4]
assert p5["ancien"] == "sans autre table\n   (VP3-06)."
p5["nouveau"] = ("sans autre table\n"
                 "   (VP3-06). Sans `--prereg`, seul un run source ni décisif ni en mode réel se lit (répétition jouet) ; un run\n"
                 "   source décisif ou en mode réel, ou dont la configuration du manifeste n'est pas un dictionnaire, est refusé sans\n"
                 "   rien écrire (liste d'arrêt). Dans tous les modes, au chargement des données du run source (en mode décisif, après\n"
                 "   les gardes ci-dessus, dont les refus restent ceux dits plus haut) : le manifeste lu sous `runs/<run source>/`\n"
                 "   porte l'identifiant de ce run ; le résumé et l'identité portent ce même identifiant ; sinon la lecture est refusée\n"
                 "   sans rien écrire (leur rattachement à l'empreinte de ce manifeste reste vérifié : sinon récupération non conforme,\n"
                 "   ligne L1). Dossier `diag/<run de lecture>` déjà présent : refus (R12), rien n'est écrit.")
p5["source"] += " ; corrigée par la vérification du module v3 (VM3-01)"

sortie.write_text(json.dumps(paires, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for k in (0, 3, 4):
    print(f"paire {k + 1} : longueurs des lignes neuves {[len(x) for x in paires[k]['nouveau'].split(chr(10))]}")
