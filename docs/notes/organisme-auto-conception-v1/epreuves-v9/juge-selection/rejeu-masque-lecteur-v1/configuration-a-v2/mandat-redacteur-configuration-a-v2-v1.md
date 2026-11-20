VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `git show --name-only`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER PAR `>`. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat du rédacteur — configuration A v2 du masque de style, rejeu du juge de sélection — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sur la décision de la mère (après R-4153, GO-2026-11-20-24 et GO-2026-11-20-28 ; la conception revient à Fable, R-3735). Le masque, joué une fois sous GO-24, a refusé : des cartes portent dans `contenu` des clés hors des dix champs de la configuration A v1. Le programme contre-lu des noms de clés, joué une fois sous GO-28, a rendu trois noms.

## Qui

Un rédacteur neuf, modèle F, qui n'a écrit ni les critères, ni le masque, ni la configuration A v1, ni le programme des noms de clés. Tu signes « rédacteur neuf, modèle F ».

## Ce que tu sais des cartes, et rien d'autre

Le seul résultat permis (`/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/rejeu-masque-lecteur-v1/jeu-noms-cles-v1/noms-cles-contenu-hors-champs-v1.json`, compagnon à vérifier) : 94 cartes ; clés de `contenu` hors des dix champs : `_` (2 cartes), `cout_note` (1 carte), `epreuve_hors_ligne` (1 carte). **Tu n'ouvres aucune carte, rien sous `archives-reponses-modeles/`, par aucune commande.** Tu ne sais pas ce que ces clés contiennent, et tu ne le cherches pas.

## Ce qui fait foi (tire de main par `fetch`, puis `git show` redirigé ; vérifie chaque empreinte)

- Critères v7 : `prereg/organisme-auto-conception-v9/juge-selection/criteres-choix-cartes-v9-v7.md` (`6af793a27f6bce4b5fe05aa18b5c6c33aed8d10a284d081fd24a0640434a316f`), en entier ; la note v7 (`bbd71b7c…`), même dossier.
- Les pièces scellées du rejeu, `prereg/organisme-auto-conception-v9/juge-selection/rejeu-v1/` : `configuration-a-masque-v1.json` (`8a8548d1444bfe3ab85396b3913c2d1b018a32541e9a283bd3f9b517a6332ce4`), `piece-scellement-manifeste-rejeu-v1.md` (`9e46ac3be599992678670e6728a057c1670bdd23de628ba94d286dbacaa6e2ad`), `manifeste-rejeu-v1.json` (`a81d30d3…`), `configuration-b-lecteur-v1.json` (`b44371d2…`).
- Le rapport v7 : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/criteres-v7/rapport-redacteur-corrections-criteres-v7-note-v7-v1.md` (`2a12a78f…`), § 5 en entier.
- Le masque : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/criteres-v4/masque_style_cartes_v1.py` (`07ed87256ba6f2ca510dfd462733190566343ed09e485cb1b638e0314780823e`) ; le lecteur par programme : `…/juge-selection/criteres-v5/lecteur_par_programme_cartes_v2.py` (`de99117b…`) : lis comment chacun traite les champs, l'ordre fixe, `intertitres`, `formules`, et ce que voient les deux lecteurs.
- Le programme qui a écrit la v1 : `…/juge-selection/candidats-manifeste-rejeu-v1/programmes/ecrire_candidats_v1.py` (`6e648318…`).
- Le compte rendu du refus : `…/juge-selection/rejeu-masque-lecteur-v1/compte-rendu-masque-et-lecteur-programme-rejeu-v1.md`.

## Ce que tu fais

1. **Pour chacune des trois clés**, propose « masquée », « ajoutée aux champs » ou « écartée », avec la raison et la règle des critères ou du rapport v7 § 5 qui l'applique (citée, ligne). Tiens compte de ce que le masque et le lecteur par programme **peuvent** faire de chaque choix (lis le code) : une clé ajoutée aux champs entre dans l'ordre fixe et dans ce que les lecteurs voient ; une clé écartée ou masquée en sort. Le nom `_` (une clé sans nom porté par deux cartes) demande une raison à part.
2. **Le nœud** : si un choix change ce que le juge voit au-delà de la règle de masquage déjà accordée (GO-2026-11-20-10, O2 ; décision 5 (a) ; confirmation 8), dis-le en tête de ta pièce, comme un nœud pour Lazar, avec options, recommandation et confiance ; écris quand même la configuration selon ta recommandation, marquée « sous réserve du nœud ».
3. **La configuration A v2**, sous le nom neuf `configuration-a-masque-v2.json`, écrite **par un programme** que tu écris dans ton dossier (outil d'écriture de fichiers ; jamais de code en ligne), qui part de la v1 à son empreinte et n'en change que ce que le point 1 décide ; il appelle `valider_configuration` du masque (chargé à son empreinte) et joint la sortie. Si le masque ne sait pas représenter un choix (par exemple écarter une clé), dis-le : c'est alors le code, ou le choix, qui change, et tu ne contournes rien.
4. Rends `proposition-configuration-a-v2-v1.md` (les trois choix, raisons, règles, nœud éventuel, différences v1 → v2, sortie de la validation) et un rapport court.

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/redacteur-configuration-a-v2/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête. Aucune carte, rien sous `archives-reponses-modeles/`. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun lancement du masque ni du lecteur sur des cartes. Aucune écriture dans le dépôt, aucun commit, aucun scellement. Rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
