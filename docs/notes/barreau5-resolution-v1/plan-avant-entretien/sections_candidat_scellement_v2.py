# -*- coding: utf-8 -*-
"""Barreau 5 : cinquième étape du candidat au scellement v2, employée par `fabrique-candidat-scellement-v2.py`.

Écrite par le rédacteur (Claude Fable 5.2). Elle s'applique au texte du premier candidat (`54bf29c3…`), sur le mot de la
mère : la section des marqueurs devient l'état au scellement. Le devis n'est pas touché. Aucune donnée du programme.
  P-1, P-2 : couples proposés au premier candidat, appliqués tels quels.
  P-3, P-4 : couples proposés, amendés comme la mère l'a demandé (état « au scellement » ; ligne `SCELLEMENT-B5F` seule ;
             phrase « rapprochement non fait au scellement », quand et par qui).
  P-5      : couple neuf, demandé par la mère (les renvois au code sont relus par la vérification du code).
  K2-*     : tenue : le statut dit ce que le candidat v2 ajoute ; le renvoi à la table de différence suit son nom neuf.
"""
import sections_candidat_scellement_v1 as SK

P = {nom: (avant, apres) for nom, motif, avant, apres in SK.PROPOSITIONS}

RETOUCHES_TEXTE = [
    ("P-1", "couple proposé, appliqué tel quel", P["P-1"][0], P["P-1"][1]),
    ("P-2", "couple proposé, appliqué tel quel", P["P-2"][0], P["P-2"][1]),
    ("P-3", "couple proposé, amendé sur le mot de la mère", P["P-3"][0],
     "## Marqueurs : état au scellement (ce texte est copié à l'octet : ce qui reste ouvert est rempli par la ligne `SCELLEMENT-B5F` du registre propre, et par elle seule, sans changer le contenu que lit le code de formation : l'empreinte du devis scellé, la tête du dépôt, les noms des sessions)\n"),
    ("P-5", "couple neuf, demandé par la mère",
     "M-5 : relecture, par le développeur, des renvois au code non rouverts par moi (`t06/lanceur.py`, `t06/identite.py`, `t07bbis/etat_impose_v1.py`, `sondes/familles.py`) ;",
     "M-5 : les renvois au code non rouverts par moi (`t06/lanceur.py`, `t06/identite.py`, `t07bbis/etat_impose_v1.py`, `sondes/familles.py`) sont relus par la vérification du code, celle du code de formation puis celle du code de lecture, et non par ce texte ;"),
    ("P-4", "couple proposé, amendé sur le mot de la mère", P["P-4"][0],
     "M-6, état au scellement : **rapprochement non fait au scellement**. Ce plan garde sa propre règle de la valeur du jumeau, écrite ici en entier ; aucune phrase du dossier ne dit que ce jumeau est celui du saboteur à budget. Le rapprochement se fera après le scellement et avant l'envoi du verdict à Lazar (`VERDICT-B5F`), par une session habilitée que la mère désigne, dans les conditions écrites ci-dessus ; son mot (« même règle », ou « autre règle » avec sa phrase d'écart) s'écrit au registre propre et ne change rien à ce plan ; s'il n'est pas fait à cette date, le verdict le dit ; M-7 : nom de la session de formation et de la session de lecture : remplis par la ligne `SCELLEMENT-B5F` ;"),
    ("K2-statut", "tenue du candidat v2",
     "quatre mentions des marques levées, nom définitif du devis. ",
     "quatre mentions des marques levées, nom définitif du devis ; et, au candidat v2, la section des marqueurs mise à l'état du scellement (premier candidat : `54bf29c3f45ae0b2b0318b275948c836bc05aaada97c22a846a64fd776892df5`). "),
]
PARTOUT_TEXTE = [("K2-table", "tenue du candidat v2", "table-difference-candidat-scellement-v1.md", "table-difference-candidat-scellement-v2.md", 2)]
