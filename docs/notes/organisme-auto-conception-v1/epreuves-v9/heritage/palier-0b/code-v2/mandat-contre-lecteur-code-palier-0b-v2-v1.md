VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET, DONNÉ CI-DESSOUS OU PAR LA TABLE DU § 7 DU RAPPORT DU DÉVELOPPEUR. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE.

# Mandat du contre-lecteur — code de l'étage sur processeur du palier 0b, version 2 — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-20. Le contre-lecteur est d'un autre modèle que le développeur (modèle S) et neuf : il n'a écrit ni le préenregistrement ni le code. Dossier du code : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/code-v2/` (noté CODE), arborescence `src/`, `tests/`, `outils-dev/`.

## Ce qui fait foi

- Le préenregistrement v6 : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/preenregistrement-heritage-palier-0b-etage-processeur-v6.md` (`4aee136b44665339be343b26913fdec8a943a0de75368013bcc4a7dc608e5029`) : annexe C, B1 à B9, « Les huit points », « Valeurs gelées », « Ordre des opérations », « Liste d'arrêt » ; son contrôle `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/controle-differentiel-palier-0b-v6-v1.md`.
- Le mandat du développeur : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/mandat-developpeur-code-palier-0b-v2.md` (`024e94e5…`).
- Le rapport du développeur : `CODE/rapport-developpeur-code-palier-0b-v2.md` (`ca61bf7e89aefe7ffe9e7a62e80ff7da1653668542f8fbd8498909a10e409b75`) ; sa § 7 donne chaque fichier et son empreinte, sa § 4 les quatorze choix pris là où le texte se tait.
- La copie de l'organisme au commit 94bfd92 : `/home/user/controle-ia-travail/docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/orchestrator/`, fichiers ouverts par les chemins que le rapport du palier 0a ou le code citent.

## Ce que tu vérifies

1. Le code fait ce que l'annexe C de la v6 dit, garde par garde de B9 ; chaque garde a un cas sain et un artefact (R5) ; aucun repli silencieux (une strate vide arrête).
2. Le défaut du bras 4b est corrigé (le multiplicateur de la tenue ne lit que la propre continuation) et son défaut réintroduit est vu.
3. Graines par `numpy.random.SeedSequence` ; les couches « décisif » et « confirmation » refusées sans autorisation ; l'essai final « aucune graine décisive dérivée » passe.
4. Lance la suite d'essais toi-même depuis une copie dans ton dossier (`cp` fichier par fichier ou `cp -r CODE/src TON_DOSSIER/src`, de même pour `tests`), avec `PYTHONPATH=src` : `python3 -B -m pytest -q -p no:cacheprovider tests/test_heritage_etage_processeur_v1_mecanique.py`, puis chaque fichier d'essais nommé au rapport, un par appel (la suite entière dure environ douze minutes : lance-la en tâche de fond et attends sa fin). Rejoue le banc des défauts `CODE/outils-dev/mutations_v1.py` et compare à ses sorties.
5. Les trois écarts au texte que le développeur n'a pas pu lever (B7 bis à la dose 0,5 ; audit de présentation sur les traits de forme ; bruit de l'audit des doses par paires) sont bien des questions de texte ou de conception, décrites justement, et non des défauts du code ; dis ce que chacun demande avant le scellement.
6. Les quatorze choix de la § 4 : chacun est un silence du texte, ou un écart à nommer.
7. Aucun tirage décisif, aucun étalonnage, aucun audit à pleine taille n'a été joué.

Verdict : « Conforme », « Conforme après corrections » (liste exacte, fichier et ligne) ou « Non conforme ».

## Ce que tu rends

Dans `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/contre-lecture-palier-0b-v2/` : `contre-lecture-code-palier-0b-v2-v1.md` et son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`). Signe « contre-lecteur, modèle S ». Le dossier courant n'est pas gardé : `env -C DOSSIER commande`.

## Interdits

Aucune commande de liste, une commande simple par appel (voir en tête). Jamais de heredoc ni de code en ligne passé à un interpréteur : un petit calcul s'écrit dans un fichier puis se lance. Aucun tirage décisif, aucun étalonnage, aucun audit à pleine taille. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif ; un calcul trop long s'arrête par l'outil de tâches. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle. Au premier refus d'un outil : arrête-toi et dis-le.
