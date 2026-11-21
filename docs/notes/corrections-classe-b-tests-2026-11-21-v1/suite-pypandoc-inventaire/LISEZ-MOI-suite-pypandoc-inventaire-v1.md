# Lot de corrections de classe B, suite — `pypandoc` et inventaire des cibles — v1

Pièce de travail (classe C), session du compte organisme, 2026-11-21 vers 21:00Z. Ce lisez-moi reprend le rapport de fin de l'agent O : il n'a pas écrit de rapport en fichier, et son rapport n'existait que dans son message de fin. Pièces non encore contre-lues par S ; rien n'est posé dans le dépôt hors de ce dossier.

## Ce qui est rendu
- `fichiers/requirements-cpu.txt` (`0f790a13…`) : version modifiée de `requirements-cpu.txt`, à poser à la place du fichier du dépôt, qui n'est pas scellé (décision de la mère du 21 novembre à 20:18Z). Ajout de deux lignes de commentaire et de `pypandoc_binary==1.17`, la même roue que la ligne 3 de `requirements-donnees.txt` (son nom d'import est `pypandoc`). Différentiel : `differentiels/requirements-cpu.txt.diff`.
- `fichiers/scripts/inventaire-cibles-invisibles-v4.json` (`ffbda4a0…`) et `fichiers/tests/test_cibles_invisibles_v4.py` (`f1bd4064248d18ccbec472cc1baf981ef44483a884205280dd42b6fd1d85708e`) : noms neufs. Différentiel de lecture du v3 vers le v4 : `differentiels/test_cibles_invisibles_v3-vers-v4.diff`.
- `outils/` : deux outils d'épreuve (transcription de l'inventaire, mutations), qui ne vont pas dans le dépôt.

## Trouvaille principale de l'agent
Une version à jour de l'inventaire existait déjà avant le tri : `tests/test_cibles_invisibles_v3.py` (`93a6df43…`, scellé, commit `5a9bd43f9`). Elle passe en entier sous `.venv`. Les 4 échecs du tri ne viennent que du v1 et du v2. Le v3 dépend toutefois du conteneur : son registre est écrit dans l'essai lui-même, et il importe `torch`, si bien qu'il ne se collecte pas sous `/usr/local/bin/python3`. Le v4 sort l'inventaire dans un fichier de données, avec un contenu inchangé (76 entrées transcrites par l'arbre syntaxique), et se joue sous les deux interpréteurs.

## Essais et mutations
- `test_cibles_invisibles_v4.py` : 18 passés sous `/usr/local/bin/python3`, 18 passés sous `.venv/bin/python`. Joué depuis une copie partielle tirée par `git archive`, effacée ensuite.
- Six mutations, toutes tuées : module retiré, lecteurs admis retirés, fichier retiré, entrée fantôme, lecteur admis mort, `import os` ajouté à l'essai. Objet faux : l'inventaire du v1, transcrit à la place du v4, rend exactement les deux messages d'échec du v1.

## Écarts et réserves dites par l'agent
- `tests/test_cibles_invisibles_v2.py` n'a pas de compagnon `.sha256` ; l'en-tête du v3 dit que le v2 a été « modifié en place ». Rien n'y est touché.
- `pypandoc_binary` n'est installé sous aucun des deux interpréteurs ; `tests/test_corpus_arxiv.py` n'a pas été rejoué.
- Le v1 et le v2 échoueront toujours : leur retrait de la suite, ou leur exemption, est à décider.
- Un fichier d'essais de plus sera hors des listes figées de T0.6, famille qui échoue déjà.
- Limites héritées du v3 : une fonction qui passerait une invite sans nom connu, ou une lecture de `cibles` par une clé construite, échapperait au détecteur.
