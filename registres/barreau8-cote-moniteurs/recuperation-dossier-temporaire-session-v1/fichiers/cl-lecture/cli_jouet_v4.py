"""Enveloppe de ligne de commande pour le jouet : appelle `lecture_sondes_v4.main(argv, cadre)` avec le cadre réduit lu dans le
fichier que nomme la variable CADRE_JOUET. Raison : la commande `python -m` de la lecture prend toujours le cadre du texte
(64 tâches, largeur 4 096, identités des vrais fichiers), qu'aucune option ne change. Cette enveloppe n'importe que le module de
la lecture : les modules `controle_ia` chargés sont les mêmes à chaque commande (bordereau du code, réception, lecture, audit)."""
import json
import os
import sys

from controle_ia.barreau8_moniteurs import lecture_sondes_v4 as L

c = json.loads(open(os.environ["CADRE_JOUET"], encoding="utf-8").read())
cadre = L.Cadre(
    tailles=L.Tailles(**c["tailles"]),
    identites=L.Identites(fichiers=c["identites"]["fichiers"], sondes=tuple(L.IdentiteSonde(**i) for i in c["identites"]["sondes"]),
                          couches_7_23=dict(L.IDENTITES_DU_TEXTE.couches_7_23)),
    recette=L.Recette(**{k: (tuple(v) if isinstance(v, list) else v) for k, v in c["recette"].items()}),
    temoin_plante=tuple(tuple(t) for t in c["temoin_plante"]), modele=c["modele"])
sys.exit(L.main(sys.argv[1:], cadre))
