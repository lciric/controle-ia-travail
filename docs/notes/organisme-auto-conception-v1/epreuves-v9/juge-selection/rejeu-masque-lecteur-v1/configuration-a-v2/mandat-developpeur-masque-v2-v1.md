VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `git show --name-only`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER PAR `>`. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat du développeur — masque de style v2 (trois clés hors des dix champs retirées et comptées), rejeu du juge de sélection — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sur **GO-2026-11-20-36**, point (1) (mot de Lazar « go recos », R-4174) : « les trois clés hors champs masquées, option (a), masque v2 codé, contre-lu, configuration A v2 scellée, masque relancé sous GO-2026-11-20-24 ». Pièce d'instrument (classe B) : contre-lue par un autre modèle, vérification des corrections par le même. **Le masque v2 est écrit et essayé sur des fichiers synthétiques ; il n'est pas joué sur les cartes** : le jeu se fera sous GO-2026-11-20-24, par un exécutant neuf, après scellement.

## Qui

Un développeur neuf, modèle O, qui n'a écrit ni le masque v1, ni la configuration A v1 ou v2, ni les critères. Tu signes « développeur, modèle O ».

## Ce qui fait foi (lis en entier ; vérifie chaque empreinte contre son compagnon par `env -C DOSSIER sha256sum -c F.sha256`)

Dossier J = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/`.
- Le masque v1 : `J/criteres-v4/masque_style_cartes_v1.py` (`07ed87256ba6f2ca510dfd462733190566343ed09e485cb1b638e0314780823e`) ; ses essais s'il y en a à côté (ouvre-les par le chemin que cite le rapport de son développeur ou la pièce de scellement).
- La proposition et la configuration A v2 : `J/rejeu-masque-lecteur-v1/configuration-a-v2/proposition-configuration-a-v2-v1.md` et `configuration-a-masque-v2.json` (`a6c5d87bf73ebcae10ff7cf87390dd4827431ce0480bbf008df755d59b3b7f54`) ; son § 3 dit les quatre choses que le masque v2 doit faire.
- Le compte rendu du refus : `J/rejeu-masque-lecteur-v1/compte-rendu-masque-et-lecteur-programme-rejeu-v1.md`.
- Sur main (`git -C /home/user/controle-ia-travail fetch origin main`, puis `git -C /home/user/controle-ia-travail show FETCH_HEAD:CHEMIN > FICHIER_DANS_TON_DOSSIER`) : `registres/go.md`, lignes GO-2026-11-20-24 et GO-2026-11-20-36 (cite-les à la lettre) ; `prereg/organisme-auto-conception-v9/juge-selection/rejeu-v1/configuration-a-masque-v1.json` (`8a8548d1…`).

## Ce que tu écris

1. `masque_style_cartes_v2.py`, nom neuf, à partir du v1, **qui ne change que** :
   - `valider_configuration` accepte une huitième clé facultative, `cles_hors_champs_retirees` : objet dont les noms sont des chaînes non vides, hors de `champs`, ni `meta` ni `empreinte`, et les valeurs des entiers d'au moins 1 ; toute autre clé neuve reste un refus ; sans cette clé, le v2 se conduit à l'octet comme le v1 ;
   - dans `extraire_contenus`, ces noms sont retirés de chaque `contenu` **avant** le contrôle « clé hors des champs » ; **toute autre clé hors des champs reste un refus** ; aucune valeur d'une clé retirée n'est lue, copiée ni écrite ;
   - refus si le nombre de cartes qui portent un nom diffère du nombre attendu (garde R5, sans repli silencieux) ;
   - le compte par clé (jamais par carte, aucun identifiant) est écrit à l'en-tête de la sortie, avec l'empreinte de la configuration ;
   - la constante d'empreinte de configuration attendue, s'il y en a une, et l'en-tête de version.
2. `essais_masque_style_cartes_v2.py`, lancés **hors du dépôt** par `env -C DOSSIER python3 -B -m pytest -q -p no:cacheprovider F`, sur des fichiers **synthétiques** que tu fabriques de la forme exacte que le masque attend : sans la huitième clé, sortie égale à l'octet à celle du v1 sur les mêmes entrées ; clé retirée sur le bon nombre de cartes ; nombre faux (en plus, en moins) ; une autre clé hors champs ; nom retiré qui est aussi un champ ; valeur 0 ou non entière ; `meta` ou `empreinte` nommé ; aucune valeur d'une clé retirée dans la sortie ni à l'écran (semée de chaînes repérables) ; compte par clé à l'en-tête. Chaque garde essayée sur un cas sain et sur un artefact (R5).
3. `differentiel-masque-v1-v2.diff` (`diff -u`, redirigé), et `rapport-developpeur-masque-v2-v1.md` : fichiers et empreintes, essais et leur sortie, ce qui change et rien d'autre, la commande unique de jeu en gabarit (à lancer plus tard sous GO-2026-11-20-24, par un autre), tout point que la lettre de GO-36 ne tranche pas, écrit en remarque.

Ton bloc-notes : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/dev-masque-v2/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête. **Tu ne touches pas au vrai fichier des cartes, ni à aucun chemin sous `archives-reponses-modeles/`, par aucune commande, même une empreinte ou `test -f`.** Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucune écriture dans le dépôt, aucun commit. Rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
