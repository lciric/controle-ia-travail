# Passation courte du développeur de la seconde passe — sous-étape 2 close (nos lentilles : registre, fiche, condition de lecture, archive) — v1

2026-11-21 (UTC), branche `claude/brave-galileo-jhp684`. Suit la passation de la sous-étape 1 (`cd67534e…`).

## Fait
- **Texte v2 lu en entier**, sans les lignes 1320 à 1343 (liste « Jamais ouverts ») : l'écart déclaré à la sous-étape 1 est réparé.
  Lus aussi : les quatre mots de Lazar nommés par le mandat et celui du 21 novembre ; les notes et la contre-lecture du lanceur v7 ;
  le registre propre (branche principale) ; de la pièce de `GO-LENTILLES-BBIS-V2`, les deux seules lignes « N12 : » et « N17 : »,
  par recherche ; du programme de comparaison version 4, les lignes rendues par une recherche des noms de champs et de libellés.
- `constantes_v2.py` (`7d62a409fcc7eee304a32d71d1b87092e00d6a176e272a6e3bf67f25db4e82de`) : texte v2, clés, nos lentilles, seuils.
- `nos_lentilles_v1.py` (`439aa06174899a7394480e391a5958925f4dcfa8885bf1fe844164278107ea03`) : lignes de la v2 et place de l'addendum ;
  état de la première passe ; issue des nœuds N12 et N17 ; fiche de rangement ; phrase du déclencheur (vi) ; condition de lecture ;
  archive de `torch.save` lue en flux (dépickleur à liste blanche, stockages factices) ; contrôles de `meta`, de l'état, des matrices ;
  contrôle de l'indice de couche de nos lentilles.
- Essais : `tests/lentilles_sondes_bbis_seconde_passe_jouets_v1.py` (`d93b79f4ecf302267fe44b9446cc775ec3f0c26ab846777e2b0dbef5f665dcb0`),
  `tests/test_lentilles_sondes_bbis_seconde_passe_nos_lentilles_v1.py` (`4c0b6b02fb9b4560a5ebaff7a32f1eb0dd2e7c90252e300a9a2b61a2d41d5e04`) :
  143 essais, verts. Essai des essais (`outils/essai-des-essais-seconde-passe-v1.py`, `outils/alterations-seconde-passe-nos-lentilles-v1.py`) :
  30 altérations, 29 vues, une équivalente.
- **Essai opposable de la forme de l'archive** : `outils/essai-forme-archive-torch-save-v1.py` et sa sortie
  `outils/sortie-essai-forme-archive-torch-save-v1.txt`, scellés. Constat neuf : torch 2.14.1 écrit `data.pkl` en premier, sans
  compression, **mais ne met pas la taille des enregistrements dans leur en-tête local** (descripteur de données après chaque
  enregistrement) ; le code tire la taille de `data.pkl` (stockages) ou du descripteur vérifié (petits enregistrements).

## Nœuds et précisions
`brouillon-noeuds-et-precisions-seconde-passe.md` (non scellé, complété au fil de l'eau) : N-dev-1 à N-dev-6.

## Reste
Sous-étapes 3 à 7. **Prochaine sous-étape exacte** : sous-étape 3, `lecture_entree_v1` (lecture par notre S, référence
« plongements seuls », chemin indépendant en double précision, garde de la fonction de lecture de notre S et de notre R, rapport à ε
étendu) et ses essais ; puis `comparaisons_lentilles_v1`.

## Expositions, instances
Aucun intitulé interdit vu hors de ceux que les pièces à lire portent elles-mêmes (le mot de Lazar du 21 novembre liste des
intitulés d'autres chaînes, sans contenu). Aucune machine, aucune dépense, aucun téléchargement de modèle, de lentille ni de corpus ;
aucune clé lue.
