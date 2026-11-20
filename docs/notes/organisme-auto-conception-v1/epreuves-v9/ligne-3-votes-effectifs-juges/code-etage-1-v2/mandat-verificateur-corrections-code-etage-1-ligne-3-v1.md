VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `grep -r`, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET, DONNÉ CI-DESSOUS.

# Mandat du vérificateur — corrections C1 à C3 du code de l'étage 1 de la ligne 3 — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-20, sur GO-2026-11-20-06 (la file reprend dans son ordre). Le vérificateur est le modèle de la contre-lecture (modèle S), neuf : il n'a écrit ni le code ni la contre-lecture.

Dossier de la ligne : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/` (noté LIGNE). Vérifie chaque empreinte contre son compagnon.

## Pièces

- Le texte qui fait foi, sur main : `git -C /home/user/controle-ia-travail fetch origin main` puis `git -C /home/user/controle-ia-travail show origin/main:prereg/organisme-auto-conception-v9/preenregistrement-ligne-3-votes-effectifs-juges-v7.md`, redirigé vers ton dossier (empreinte commençant par `4e3680d9`).
- La contre-lecture : `LIGNE/code-etage-1-v1/contre-lecture-v1/contre-lecture-code-etage-1-ligne-3-v1.md` (`3aed6849c76a4ed421207470e4a6b8a45fcecf6a8ef5325a5203c84fda2f85ff`), ses mutants `LIGNE/code-etage-1-v1/contre-lecture-v1/mutants_cl.py`.
- Le code v1 : `LIGNE/code-etage-1-v1/banc_juges_scriptes_ligne_3_v1.py`, `LIGNE/code-etage-1-v1/essais_banc_juges_scriptes_ligne_3_v1.py`.
- Le mandat du développeur : `LIGNE/mandat-developpeur-code-etage-1-ligne-3-v3.md` (`8d7e9a36bd4c4cf7aaaad49c3a9dd69996f40b5b3f7e7657dc101ed2d246a281`).
- Le code v2, dans `LIGNE/code-etage-1-v2/` : `banc_juges_scriptes_ligne_3_v2.py` (`ffc33083…`), `essais_banc_juges_scriptes_ligne_3_v2.py` (`d90eb6f3…`), `chronometrer_banc_ligne_3_v2.py` (`9bcea530…`), `controle_defauts_reintroduits_ligne_3_v2.py` (`1ead2775…`), `rapport-defauts-reintroduits-ligne-3-v2.json` (`09f089cf…`), `rapport-defauts-reintroduits-fichier-entier-ligne-3-v2.json` (`fde1277c…`), `rapport-developpeur-code-etage-1-ligne-3-v2.md` (`995bd5f4…`) ; les journaux de l'outil de remplacement dans `LIGNE/code-etage-1-v2/journaux-remplacements/` : `banc_juges_scriptes_ligne_3_v2.py.journal-remplacements-v1.json`, `chronometrer_banc_ligne_3_v2.py.journal-remplacements-v1.json`, `essais_banc_juges_scriptes_ligne_3_v2.py.journal-remplacements-v1.json`, `controle_defauts_reintroduits_ligne_3_v2.py.journal-remplacements-v1.json`.

## Ce que tu vérifies

1. C1, C2, C3 sont appliquées comme la contre-lecture les demande ; C2 suit la lettre « à partir de laquelle ».
2. Le différentiel v1 → v2 du banc et du chronomètre ne touche que ce que C2 demande (compare par `diff -u` du v1 au v2, fichiers nommés un par un) ; aucun tirage ne change.
3. Lance les essais toi-même depuis une copie dans ton dossier : `python3 -B -m pytest -q -p no:cacheprovider CHEMIN_DES_ESSAIS_V2` ; rejoue le contrôle des défauts réintroduits ; dis combien sont vus, dont les 35 mutants.
4. Graines : seule la racine 2026111930 est dérivée ; aucune de 2026111931 à 2026111937.
5. Les questions de texte laissées par le développeur sont bien des silences du texte, pas des écarts du code.

Verdict : « Conforme », « Conforme après corrections » (liste exacte, fichier et ligne) ou « Non conforme ».

## Ce que tu rends

Dans `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/verification-ligne3-etage1-v2/` : `verification-corrections-code-etage-1-ligne-3-v1.md` et son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`). Signe « vérificateur, modèle S ». Le dossier courant n'est pas gardé d'un appel à l'autre : utilise `env -C DOSSIER commande`.

## Interdits

Aucune commande de liste (voir en tête). Jamais de heredoc ni de code en ligne passé à un interpréteur — un petit calcul s'écrit dans un fichier puis se lance ; une commande simple à la fois. Aucun calcul décisif, aucun chronomètre à pleine taille. Aucune écriture dans le dépôt, aucun commit. Aucune commande, même une empreinte, sur un chemin sous `archives-reponses-modeles/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle. Au premier refus d'un outil : arrête-toi et dis-le.
