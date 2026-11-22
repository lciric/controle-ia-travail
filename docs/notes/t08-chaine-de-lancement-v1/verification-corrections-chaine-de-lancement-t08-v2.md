# Vérification de la chaîne de lancement de T0.8 au commit C — v2

- **Nature** : vérification courte (classe B), même contre-lecteur que la contre-lecture (`e52658a2…`) et la vérification v1 (`d0d2923e5cc93790764a4a9e2237adaab85697a341d4774be0ec780ecac4d812`, valable au commit `c061e40b2`) ; la v1 reste telle quelle (R12).
- **Contre-lecteur** : session `session_013QMaymC2hofayrH8ySBw7N` (Opus 5.5), le 2026-11-22 vers 22:45 à 23:00 UTC.
- **Pièce** : commit C = `bd32f9a5c3edede9ac2fad36946750b322303687`, descendant de `c061e40b2` ; différentiel `c061e40b2..bd32f9a5c`.
- Aucune machine, aucun appel au loueur, aucune dépense ; aucun résultat de course ni verdict lu.

## Avis

**Conforme : la chaîne est scellable au commit C.** r-9 est tenu ; les empreintes de P7 sont confirmées.

## Différentiel `c061e40b2..bd32f9a5c` sur la chaîne

Dans `src/`, `scripts/`, `tests/`, `.claude/`, `pyproject.toml`, `requirements-*.txt`, `.gitignore` et les autres chemins que l'amorce extrait, **seuls trois fichiers changent**, avec leurs compagnons (tous trois vérifiés) :
- `scripts/amorce_instance_t08_v1.sh` : `ATTENDUS="252"` devient `"255"`, et le commentaire du clonage dit 255 ; rien d'autre.
- `scripts/ecrire_configuration_lecture_t08_v1.py` (r-9) : `resultat.fichiers` doit être un dictionnaire ; chacun des six fichiers de la course doit y porter une empreinte de 64 caractères hexadécimaux, sinon arrêt, rien d'écrit ; ce fichier entre dans la liste blanche à cette empreinte (inchangé), et `course-t08.json` reste vérifié contre son compagnon et contre la ligne `COURSE-T08` (inchangé). Plus en-tête (r-9, `GO-2026-11-22-134`) et `import re`.
- `tests/test_t08_chaine_lecture_v1.py` : les essais de r-9.

Le reste du différentiel touche des documents (brouillons, procédures, contre-lectures, passations) et `registres/go.md` : 31 lignes neuves, et les lignes `GO-2026-11-22-98` et `-106` corrigées. Les lignes `GO-2026-11-10-12` et `GO-2026-11-22-79` ne changent pas. La fonction de lecture du registre de la garde de calcul (`lire_go`, au commit C) lit tout le fichier (741 lignes), sans erreur. Je l'ai appelée directement : le crochet de ma session, qui lit le registre plus ancien de ma branche, bloquait toute commande portant le motif de création, et je ne l'ai pas contourné.

**r-9 conforme** à `GO-2026-11-22-134`. Un fichier recomposé de morceaux n'entre à la lecture que s'il est égal à l'octet à la sortie scellée, à l'empreinte que donne `course-t08.json`. Cette enveloppe est elle-même tenue par la ligne `COURSE-T08` et par son compagnon. Le compagnon seul ne suffit plus.

## Empreintes de P7 au commit C (confirmées)

- `fe279aba85587d3ae1653b67d193aa3faab93093c350cc4c82ad217158c61c91` `scripts/amorce_instance_t08_v1.sh`
- `acfe5a757a626f6f254527d7f0009e2af43b5b95833c7fd1cbe68f2f9bf7b03c` `scripts/lancer_t08_v1.sh`
- `051c73d23ec85668d263165e089643c9792970d1d6f05d30e3de7fdb133a76cc` `scripts/construire_branche_entree_t08_v1.py`
- `5b6db29b7434c3bd38c6178d04b790572e96f767c1ba36410694fcb2a0000c2c` `scripts/tests-cibles-t08-v1.txt` (égale à `LISTE_SHA256` de l'amorce)
- en plus (remarque n-2a de la v1) : `bce5f4c9ae82eeb10d90b9cfd4c86ce6b061ac1deb0182723d67d30830dbdb0e` `src/controle_ia/lancement_t08/session_v1.py` ; `6b2a219f78e07c4527adea175729ece15178a60a5896032d7c912c8e11885749` `scripts/ecrire_configuration_course_t08_v1.py` ; `994c3bfa34cf1bb6a4597373a8d5147d7be214bf511339e0ffeb1aa331cf932c` `scripts/ecrire_configuration_lecture_t08_v1.py`.

## Essai rejoué au commit C

Liste figée (13 fichiers), avec l'essai que l'amorce écarte désélectionné comme sur la machine : **255 passés, 1 désélectionné**, 207 s. C'est le nombre `ATTENDUS` de l'amorce. Je n'ai pas rejoué l'essai écarté à C : ni son fichier ni le code ne changent depuis `c061e40b2`, où il passait.
