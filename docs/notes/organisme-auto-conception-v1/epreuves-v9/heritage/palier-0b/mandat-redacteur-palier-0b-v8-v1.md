VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER DE TON DOSSIER, JAMAIS À L'ÉCRAN.

# Mandat du rédacteur — préenregistrement du palier 0b, version 8 (corrections du contrôle de la v7) — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-20. Dossier : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/` (noté P0B).

## Qui

Un rédacteur neuf, modèle F. Tu signes « rédacteur neuf, modèle F ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

- Le contrôle : `P0B/controle-differentiel-palier-0b-v7-v1.md` (`1211fed3b3ce0baa2324c1976897dda622e9fabc91c6ccbe50ea110346db19d0`), verdict « Conforme après corrections » : **seize remplacements** (corrections 1 à 16), texte ancien et neuf au § 9 ; ses réponses aux trois questions de la mère (R-4076), § 4, à reprendre dans l'annexe H en tête des nœuds 1 et 2 ; ses remarques non bloquantes, § 10. Le calcul de la réserve 23 : `P0B/controle-v7-outils/calcul_reserve_23_v1.py` et sa sortie.
- La v7 : `P0B/preenregistrement-heritage-palier-0b-etage-processeur-v7.md` (`2f0f928f…`) et le rapport `P0B/rapport-redacteur-palier-0b-v7-v1.md` (`c06c2870…`).

## Ce que tu fais

1. Les seize corrections **à la lettre**, par l'outil contre-lu (`python3 -B /home/user/controle-ia-travail/scripts/remplacer_texte_exact_v1.py`, empreinte commençant par `391db990`), un JSON écrit avec l'outil d'écriture de fichiers, sous le nom neuf `preenregistrement-heritage-palier-0b-etage-processeur-v8.md`. Tenue : titre, ligne de version.
2. Dans l'annexe H, en tête des nœuds 1 et 2, la réponse aux trois questions de R-4076 telle que le contrôle l'établit (d'où venait ce que le rédacteur savait ; dépendance ou non de chaque règle à l'attente d'un arrêt ; ce que dit la v6 de ce cas), avec les options qui n'en dépendent pas — sans trancher ; si cela demande un texte que le contrôle ne donne pas mot pour mot, écris-le et déclare-le.
3. La liste de ce qui demande un code v4, complétée par les remarques du § 10 qui touchent le code (dont : où se joue le jeu de la garde 27 ; le fichier d'autorisation de D6 à définir ; l'exactitude « non calculée » qui arrête).
4. Différentiel `diff -u` v7 → v8 et rapport `rapport-redacteur-palier-0b-v8-v1.md`.

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/redacteur-palier-0b-v8/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`). Le dossier courant n'est pas gardé : `env -C DOSSIER commande`. Règle R-4067 : si l'outil rejette une ancre, c'est un essai qui échoue ; JSON neuf (nom neuf), fautif gardé, incident déclaré ; vérifie chaque ancre par `grep -c -F -e` sur la cible avant l'appel.

## Interdits

Voir en tête. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun tirage, aucun lancement du code de l'étage. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
