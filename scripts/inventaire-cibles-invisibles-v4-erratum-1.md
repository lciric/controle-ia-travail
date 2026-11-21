# Erratum 1 à `scripts/inventaire-cibles-invisibles-v4.json` — v1

Pièce de travail (classe C), session du compte organisme, 2026-11-21 vers 22:00Z, à verser sur `main` par la mère, qui l'a demandé dans son message de 21:55Z. Le fichier visé reste intact.

- **Fichier visé** : `scripts/inventaire-cibles-invisibles-v4.json`, versé sur `main` par la mère (R-4735), empreinte `ffbda4a0ef2632dd9e91aecb62205a9830ec1f83e9f5fd782e1f5f13eadef878`.
- **Champ** : « source ».
- **Texte actuel** : « transcription mécanique de tests/test_cibles_invisibles_v3.py (REGISTRE, LECTEURS_DE_CIBLES_ADMIS, HORS_INVENTAIRE), sans changement de contenu ; lue par tests/test_cibles_invisibles_v4.py ».
- **À lire** : « … ; lue par tests/test_inventaire_cibles_organisme_v1.py ».
- **Pourquoi** : l'essai qui lit cet inventaire a été renommé, parce que son nom d'origine entrait en collision avec un autre `tests/test_cibles_invisibles_v4.py` déjà présent sur `main` (message de la mère de 21:45Z). Le contenu de l'essai est inchangé (`f1bd4064…`). L'essai renommé reste sur la branche `lot/compte-organisme-v1` (décision de la mère de 21:55Z, voie (a)) : sur l'arbre de `main`, il signale environ soixante constructeurs d'invite que la branche n'a pas, et n'est donc juste que sur la branche.
- **Conséquence** : sur `main`, aucun essai ne lit ce fichier aujourd'hui. Une version 2 de l'inventaire, établie sur l'arbre de `main`, devra soit le lire, soit le remplacer.
