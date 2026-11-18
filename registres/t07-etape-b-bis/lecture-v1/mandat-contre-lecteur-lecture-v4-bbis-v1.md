# Mandat du contre-lecteur du module de lecture neuf (`lecture_v4`) — apprentissage des sondes sur la tâche (étape B bis de T0.7) — v1

Tu es un sous-agent neuf, d'un autre modèle que le développeur ; tu n'as écrit ni l'addendum ni le code. Lis d'abord `registres/t07-etape-b-bis/lecture-v1/regles-communes-agents-lecture-bbis-v1.md` : il te lie.

## Ce qui fait foi
`prereg/T0.7-etape-B-bis-v1-addendum-ecart-4-v1.md` (empreinte `5ef929eae8b070bc7f9d1934d487066ded34896df00dc8a9c70c91b44f0b30c4`), § 2.0, QA-1 à QA-4, § 6 ; le texte scellé `prereg/T0.7-etape-B-bis-v1.md` et ses trois premiers addenda là où le quatrième y renvoie ; la note n4 de `brouillons/T0.7-etape-B-bis-v1/contre-lecture-addendum-ecart-4-brouillon1-v1.md`.

## Ce que tu vérifies
1. `src/controle_ia/t07bbis/lecture_v4.py` ne diffère de `lecture_v3.py` (empreinte `c9a478437f32465418dfafdadbd7823f88853a9c17f77a0e59cc4ccb5ccff6ec`) **que** par les différences que le § 6.1 déclare (refais le `diff -u` toi-même ; compare à `registres/t07-etape-b-bis/lecture-v1/differences-lecture-v3-v4-bbis-v1.md`). Tout bloc changé sans fondement : constat majeur. Aucun fichier existant modifié (`git status`, `git diff --stat`).
2. Chaque différence fait ce que l'addendum dit, et pas plus : l'exception d'égalité à la seconde ne vaut que pour les deux lignes épinglées (dates, chemins, empreintes), sous la preuve d'entrée conjointe relevée par programme ; la chaîne d'ordre continue après l'exception ; toute autre égalité, toute inversion, la même égalité sans la preuve restent un refus ; la preuve lève le refus de lecture, non l'arrêt de garde ; aucun repli silencieux ; aucun mode neuf ; rien n'élargit la lecture (entrées, graines, critères, phrases, ordre inchangés).
3. La preuve ne peut pas passer à tort : histoire tronquée, commit absent, lignes changées d'un octet, fiche ou accord changés, autre parent, autre branche. Elle ne peut pas refuser à tort sur l'histoire telle que le § 2.0 la décrit (par lecture du code contre les faits du § 2.0 — **sans la jouer sur le dépôt réel**).
4. `tests/test_t07bbis_lecture_v4.py` porte chaque essai du § 6.2 (cas sain et chaque artefact), sur jouets seulement ; aucun essai ne touche un fichier réel ou l'histoire réelle. Rejoue-les : `python -m pytest -q tests/test_t07bbis_lecture_v4.py --basetemp=<dossier temporaire de la session>/basetemp-v4-cl` (interpréteur `.venv/bin/python` s'il existe, `PYTHONPATH=src`), dossier supprimé après ; puis les essais existants `tests/test_t07bbis_*.py`.
5. S'il y a un mode « garde seule » : il ne doit pas exister (§ 6.5).

## Interdits fermes
Tu ne joues jamais le module, sa garde ni aucune de ses fonctions sur les fichiers réels (registre propre, histoire git réelle, sorties, entrées), sous aucune forme — une telle commande a été refusée par le classifieur à un autre agent. Aucun fichier de résultat ouvert ; pas de commit ; tu ne corriges pas le code. Au premier refus : arrêt, texte exact rendu.

## Rendu
Fichier scellé `registres/t07-etape-b-bis/lecture-v1/contre-lecture-lecture-v4-bbis-v1.md` : constats numérotés (majeur / mineur / note), chacun fondé sur une ligne du code et une ligne de l'addendum ; empreintes des fichiers contre-lus ; conclusion en un mot : « rattachable », « rattachable après corrections mineures » (liste exacte) ou « non rattachable ». À la conductrice : chemin, empreinte, conclusion, nombre de constats par niveau, essais passés ou non, fichiers ouverts.
