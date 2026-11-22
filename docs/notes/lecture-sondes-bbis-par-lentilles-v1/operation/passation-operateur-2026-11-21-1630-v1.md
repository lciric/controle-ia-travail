# Passation de l'opérateur neuf de la lecture des sondes de l'étape B bis par la lentille publique — 2026-11-21 16:30Z — v1

Pièce de travail (classe C). Opérateur : session ouverte par la mère (`session_01Qi7Gr3eYmAhDEJzqLgWcv1`), révision `c8c6d2aa`, mandat v2
(`90f8befb…`, vérifié), fiche du code (`a44c0e54…`, vérifiée). Aucune table, aucun `arret.json`, aucune sortie de l'étape B bis ouverts.

## Fait
- Préalables : mandat, fiche du code, texte scellé v1 (`ca5066d7…`), extrait `GO-LENTILLES-BBIS` (`8a68e335…`) aux empreintes attendues ;
  `SCELLEMENT-`, `GO-`, `CODE-LENTILLES-BBIS` présentes au registre propre ; `SCORES-BBIS` une fois, `VERDICT-BBIS` présente
  (registre de l'étape B bis). Clé de la plateforme présente (testée sans impression). Recherche de dossiers de course : vide.
  4 fils, 15 Go de mémoire, 60 Go libres.
- Correctifs (2), (4), (6) extraits un par un de `claude/brave-galileo-jhp684` (commit `d0fa985a`) : trois empreintes égales au texte.
  Copie versée de `readout.py` : `2c0fe995…`, égale.
- Environnement : `requirements-cpu.txt` ; paquets manquants installés à versions épinglées (texte, point 4, « environnement ») :
  `datasets==5.2.0` (apporte `pyarrow 26.0.1`), `requests==2.34.2`.
- Montage, course `20261121-161858-lentilles-bbis-v1` : échec d'importation (`requests` absent), avant toute requête ; journal
  `montage.log` (`65006848…`). Dossier de travail laissé (marque seule, 8 Ko), rien supprimé.
- Montage, course `20261121-161939-lentilles-bbis-v1` : **arrêt nommé du code**, code 3 :
  « jeu de données de la tranche zh : aucun fichier de données dans l'arbre : arrêt ; nœud » ; journal `montage-2.log` (`5044829…`).
  Essais d'un octet de la lentille, du fichier de poids à porte et du dépôt voisin passés ; voisin cloné au commit `849bfe16…`,
  correctifs appliqués. Aucun poids ni lentille téléchargé ; aucun dossier de sortie créé. Dossier de travail laissé (marque et
  clone du voisin, 33 Mo), rien supprimé.

## Diagnostic (requête publique sans clé, métadonnées seules)
L'arbre de `HuggingFaceFW/fineweb-2` à la révision `af9c1333…` (`?recursive=true`) est **paginé** : 1000 entrées par page, en-tête
`link: …; rel="next"`. La première page ne porte que des dossiers (`data/aai_Latn`, …), aucun fichier. `cibles_corpus`
(`montage_v1.py`, l. 633-654) ne lit que la première page : défaut du code (classe B), hors de mon mandat.

## Reste
Nœud à la mère : correction du code (suivi de la pagination, ou requête de l'arbre restreinte au dossier de la configuration
`data/cmn_Hani/train`), contre-lecture, nouvelle fiche et nouvelle ligne `CODE-LENTILLES-BBIS`, puis montage neuf avec un identifiant
de course neuf. Je ne relance rien avant le mot de la mère.

## Instances actives
Aucune machine louée. Aucun processus du lanceur vivant.
