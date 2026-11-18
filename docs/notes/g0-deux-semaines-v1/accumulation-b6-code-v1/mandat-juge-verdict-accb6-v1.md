# Mandat du juge neuf du verdict du barreau 6 (accumulation sur l'épisode) — v1

Écrit par la session mère `session_013QMayjsoZJFBUCqcnvD5h1` le 2026-11-18 vers 17:20Z (GO-2026-11-18-30 ; R13 par analogie : verdict prononcé par un agent neuf qui applique les critères gelés). Langue : français, sans sigle seul (nommer chaque chose par ce qu'elle est).

## Qui tu es
Un **juge neuf** : tu n'as écrit ni le texte du barreau 6, ni son code, ni ses contre-lectures, ni joué sa lecture ; tu n'as lu aucun résultat de P3-bis ; tu ne prononces que ce que les critères gelés disent. Tu n'ajoutes aucune analyse non prévue.

## Ce que tu lis
- Le texte scellé `prereg/accumulation-barreau6-v1.md` (`2e2dddc60667cd5c670a37a656e896cc210e59ac92be37211bbb1680fc1a4b22`, vérifie l'empreinte) en entier, en particulier « Prédiction chiffrée », « Métrique », « Seuil », « Plan d'analyse », **« Critères de lecture gelés »**, « Liste d'arrêt », « Lignes de registre ».
- La lecture écrite par le programme, dans l'arbre de la lecture : `/home/user/accb6-racine-v1/diag/20261118-171021-accb6-lecture/lecture-accb6.json` (`096a3f62a70aa7d14de01a9401e6db0edb2b65603190b74ae80ac5696572e7c8`, vérifie l'empreinte et le compagnon) ; son manifeste `/home/user/accb6-racine-v1/runs/20261118-171021-accb6-lecture/manifeste.json` (`4aac26b4…`) ; la ligne `LECTURE-ACCB6` de `registres/accumulation-b6-v1.md` (`c675531f…`).
- Tu peux ouvrir la sortie standard de la lecture (`/home/user/accb6-racine-v1/sortie-standard-lecture-accb6-v1.txt`, `e8443c1a…`) si le texte le prévoit ; sinon non.
- Rien d'autre du programme : aucun autre résultat, aucune autre sortie (étape B, étape B bis, P3-bis…), rien sous `docs/verdicts/` hors de ce que le texte cite ; pas de recherche récursive.

## Ce que tu rends
- Un **verdict** au format que le texte prescrit (sinon : un fichier markdown), sous `docs/verdicts/verdict-accb6-v1.md` dans le dépôt principal `/home/user/controle-ia-travail`, **scellé** (`PYTHONPATH=src python3 -m controle_ia.scellement sceller <fichier>`) : l'issue de chaque prédiction selon les critères gelés, les chiffres qui la fondent (recopiés de la lecture, avec leur clé), les réserves que le texte prévoit, la liste d'arrêt vérifiée ; et **une phrase en clair** pour Lazar (sans sigle seul).
- Si le texte prescrit une ligne de registre de verdict (par exemple dans `registres/accumulation-b6-v1.md`), écris-la **seulement** si le texte le dit, avec chemin et empreinte du verdict.
- Ne commite pas, ne pousse pas ; n'écris pas dans `registres/decisions.md`.
- **Ton dernier message à la session mère ne contient AUCUN résultat** : seulement « verdict écrit », le chemin et l'empreinte du verdict, la ligne de registre écrite le cas échéant (chemin et empreinte du registre), et toute lecture faite hors de ce mandat. La mère ne lit pas le verdict : elle le porte à Lazar par son chemin.
