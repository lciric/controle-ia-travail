# Mandat du développeur du module de lecture neuf (`lecture_v4`) — apprentissage des sondes sur la tâche (étape B bis de T0.7) — v1

Tu es un sous-agent neuf. Lis d'abord `registres/t07-etape-b-bis/lecture-v1/regles-communes-agents-lecture-bbis-v1.md` : il te lie (cloisonnement, rendu sans mesure, arrêt au premier refus).

## Ce qui fait foi pour toi
Le quatrième addendum d'écart, scellé : `prereg/T0.7-etape-B-bis-v1-addendum-ecart-4-v1.md`, empreinte `5ef929eae8b070bc7f9d1934d487066ded34896df00dc8a9c70c91b44f0b30c4` (vérifie le compagnon). Son § 6 est ta spécification : § 6.1 (spécification exacte : copie de la version 3 plus les différences déclarées, et rien d'autre), § 6.2 (essais exigés, cas sain et artefacts, R5), § 6.3 (contre-lecture et rattachement), § 6.4 (preuve relevée à part), § 6.5. Lis aussi QA-1 à QA-4 et le § 2.0 (les faits : lignes, empreintes, commits que la preuve épingle). La consigne de la note n4 de `brouillons/T0.7-etape-B-bis-v1/contre-lecture-addendum-ecart-4-brouillon1-v1.md` (la preuve lève le refus de lecture, non l'arrêt de garde) est à suivre.

## Ta tâche
1. Écrire `src/controle_ia/t07bbis/lecture_v4.py` : **copie de `lecture_v3.py`** (empreinte `c9a478437f32465418dfafdadbd7823f88853a9c17f77a0e59cc4ccb5ccff6ec`) **plus les différences que le § 6.1 déclare, et aucune autre**. Aucun fichier existant n'est modifié (R12) ; `lecture_v1`, `v2`, `v3` restent. Aucun mode « garde seule » (§ 6.5) ; la garde s'exécute en tête de la lecture, comme dans la version 3.
2. Écrire `tests/test_t07bbis_lecture_v4.py` : les essais du § 6.2, **sur registres et dépôts git jouets seulement**, fabriqués dans le dossier temporaire de l'essai (`tmp_path`). Aucun essai ne lit le registre propre réel, une sortie de la course, une entrée de 7b ni l'histoire réelle du dépôt.
3. Jouer : `python -m pytest -q tests/test_t07bbis_lecture_v4.py --basetemp=<dossier temporaire de la session>/basetemp-v4` puis les essais existants de la chaîne (`tests/test_t07bbis_*.py`) pour constater que rien n'est cassé ; dossier `--basetemp` supprimé après. Interpréteur : `.venv/bin/python` du dépôt s'il existe, `PYTHONPATH=src`.
4. Écrire `registres/t07-etape-b-bis/lecture-v1/differences-lecture-v3-v4-bbis-v1.md` : la sortie de `diff -u` entre la version 3 et la version 4, et, pour chaque bloc changé, la différence du § 6.1 qui le fonde ; tout bloc sans fondement = faute à corriger avant de rendre.
5. Sceller les trois fichiers (`python -m controle_ia.scellement sceller`).

## Interdits fermes
- **Tu ne joues jamais le module, sa garde, ni aucune de ses fonctions sur les fichiers réels** (registre propre, registres du dépôt, histoire git réelle, sorties de la course, entrées) : ni par `main()`, ni par un script à blanc, ni dans un essai, ni dans un interpréteur. Une commande de ce genre (essai à blanc d'une garde d'ouverture sur l'arbre principal) a été refusée par le classifieur à un autre agent : ne la rejoue sous aucune forme, ni entière ni découpée.
- Aucun fichier de résultat ouvert ; pas de commit, pas de poussée ; aucune dépense ; aucune installation de paquet.
- Si la spécification est ambiguë ou qu'une différence nécessaire n'y est pas déclarée : tu ne l'ajoutes pas ; tu l'écris comme point ouvert et tu t'arrêtes sur ce point.
- Au premier refus du classifieur, d'une permission ou du crochet : arrêt, texte exact rendu.

## Rendu
Chemins et empreintes des trois fichiers ; nombre d'essais neufs, passés ou non (noms des essais en échec, sans valeur de mesure — il n'y en a pas sur des jouets) ; essais existants : passés ou non ; nombre de blocs changés et, pour chacun, la différence qui le fonde ; points ouverts ; fichiers ouverts.
