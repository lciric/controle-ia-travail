VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. AUCUNE RECHERCHE DE MOTIF LARGE : OUVRE LES FICHIERS PAR CHEMIN ET PAR PLAGES DE LIGNES.

# Mandat du rédacteur — consigne des lecteurs du rejeu, version 2 (corrections K1 à K4) — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-20. Dossier : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/consigne-lecteurs-v1/` (noté C).

## Qui

Un rédacteur neuf, modèle F. Tu signes « rédacteur neuf, modèle F ».

## Règle d'or

Aucune carte ouverte, aucun fichier de cartes ni de sélection, rien sous `archives-reponses-modeles/`.

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

- La consigne v1 : `C/consigne-lecteurs-rejeu-criteres-v7-v1.md` (`bf49bd50…`) et son rapport `C/rapport-redacteur-consigne-lecteurs-rejeu-v1.md`.
- La contre-lecture : `C/contre-lecture-consigne-lecteurs-rejeu-v1.md` (`d9f5ff4cb6a741db6dad195316bdbb16f841b478f3fb416d0b72e54478898f5c`), corrections **K1 à K4**, texte exact au § 8 ; sa réserve sur l'amorçage par le signal du rejeu v2.
- La confirmation X6 : `C/confirmation-x6-cartes-attendues-v1.md` (`040b83a1…`) : 94 cartes, `hors_choix` vide ; si la consigne parle du nombre de cartes ou de `hors_choix`, elle doit le dire ainsi.
- Les décisions de la mère : le contrôle de `lignee_reconnue` est un programme de garde à part, joué avant `assembler` (la consigne peut dire qu'une valeur hors des six chaînes sera refusée) ; l'étiquette la plus probable entre `prop-opus` et `prop-fable` vaut quand la lignée n'est pas sûre. Pour K1 (limite en tête de `independance` plutôt qu'en note de dépôt), applique K1 tel que la contre-lecture l'écrit ; la note de dépôt reste, avec K4.

## Ce que tu fais

1. K1 à K4 **à la lettre**, par l'outil contre-lu (`python3 -B /home/user/controle-ia-travail/scripts/remplacer_texte_exact_v1.py`, empreinte commençant par `391db990`), un JSON écrit avec l'outil d'écriture de fichiers, sous le nom neuf `consigne-lecteurs-rejeu-criteres-v7-v2.md` ; tenue : titre, ligne de version ; la phrase sur le refus par la garde et sur 94 cartes si la consigne en parle. Aucune autre modification.
2. Différentiel `diff -u` v1 → v2 et rapport court `rapport-redacteur-consigne-lecteurs-rejeu-v2-v1.md`.

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/redacteur-consigne-lecteurs-rejeu-v2/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`). Règle R-4067 pour l'outil ; vérifie chaque ancre par `grep -c -F -e` sur la cible avant l'appel.

## Interdits

Voir en tête. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucune carte. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
