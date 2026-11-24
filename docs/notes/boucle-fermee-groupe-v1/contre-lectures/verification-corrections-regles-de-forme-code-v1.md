# Vérification des corrections — règles de forme (même contre-lecteur)

Lu sur disque : `src/controle_ia/prereg.py` (diff), gabarit v2, tests. 17 tests passent (`PYTHONPATH=src python3 -m pytest -q tests/test_prereg_forme_v2.py tests/test_prereg.py`). Gabarit v1 : `git diff origin/main` vide. Fonctions v1 de `prereg.py` inchangées (ajouts seulement, plus `import unicodedata`). Essais jetables dans le bloc-notes.

## Verdict : tient, une régression mineure

| Point | Statut | Preuve |
|---|---|---|
| 1 gabarit renvoie à `sceller_prereg_v2`, `exiger_prereg_scelle_v2` ajoutée | tenu | gabarit l.12 ; la fonction enchaîne la garde v1 puis `problemes_forme` |
| 2 puces avec continuation | tenu pour le texte continu | règle « Label :⏎  effectif 200 puissance 0,8 » : aucun problème |
| 3 NFC, apostrophe, casse, deux-points dans le gras, puces `*` et numérotées | tenu | essais `* **Label :**`, `1. **label**`, `Lot d’étalonnage` : aucun problème |
| 4 marqueur insensible à la casse | tenu | « à remplir plus tard svp » refusé |
| 5 bouche-trous refusés, limite dite | tenu | `TODO TODO TODO`, `n/a n/a n/a`, `sans objet : n/a n/a n/a`, « voir plus tard » refusés ; limite dite au docstring/gabarit |
| 6 toutes les occurrences validées | tenu | boucle sur `valeurs` (prereg.py, bloc `for valeur in valeurs`) |
| Mineures : tiret long, « sans objet » nu, section en double, « non exécutable » non vérifié | tenues | « Sans objet — pas de test ici » accepté ; « sans objet » nu : « sans raison » ; section en double signalée ; gabarit l.18 le dit |

## Remarque restante

1. **Mineure (régression de la correction 2)** — `prereg.py`, `_puces` : une sous-liste sous une règle (`- **Effectif…** :` puis `  - effectif 200`, `  - puissance 0,8`) est lue comme de nouvelles puces ; la règle est alors jugée « vide ou à remplir » (faux positif, refus sûr), et les sous-puces sont perdues. Correction : ne démarrer une puce de règle que si la ligne commence par `**` après la puce, sinon traiter la ligne comme continuation ; ou documenter « pas de sous-liste ». Un test à ajouter.
2. **Mineure** — un paragraphe non puce placé après la dernière règle est collé à celle-ci (continuation) ; sans conséquence tant que le mot-marqueur n'y figure pas ; à noter.

Aucune autre régression relevée.
