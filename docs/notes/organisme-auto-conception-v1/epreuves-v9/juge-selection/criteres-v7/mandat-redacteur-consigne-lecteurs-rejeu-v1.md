VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER DE TON DOSSIER, JAMAIS À L'ÉCRAN.

# Mandat du rédacteur — consigne des deux lecteurs du rejeu du juge de sélection (critères v7) — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-20, sur la demande de la mère (texte de lecture, rédigé par un rédacteur de modèle F, R-3735 ; contre-lu par un autre modèle). Dossier : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/` (noté JUGE).

## Qui

Un rédacteur neuf, modèle F. Tu signes « rédacteur neuf, modèle F ».

## Règle d'or

Aucune carte ouverte, aucun fichier de cartes ni de sélection, rien sous `archives-reponses-modeles/`. Tu écris une consigne ; tu ne lis aucune carte.

## Ce qui fait foi (vérifie chaque empreinte)

- Les critères v7 et la note v7, scellés sur main : `git -C /home/user/controle-ia-travail fetch origin main`, puis `git -C /home/user/controle-ia-travail show origin/main:prereg/organisme-auto-conception-v9/juge-selection/criteres-choix-cartes-v9-v7.md` et `…/note-conception-juge-selection-cartes-ecartees-v7.md`, redirigés vers ton dossier (empreintes `6af793a2…` et `bbd71b7c…`). Annexe A (format d'une lecture déposée), annexe B, annexe C (ordre des gestes), § 8 (veto).
- La table finale du manifeste : `JUGE/criteres-v7/table-manifeste-rejeu-apres-go-2026-11-20-10-v1.md` (`a41a2c7c…`), sa réserve sur `lignee_reconnue` ; les réponses sur les familles : `JUGE/criteres-v7/reponses-familles-et-champ-x6-v1.md` (`35cc9bcf…`).
- Les décisions de Lazar (GO-2026-11-20-10, O2, sur main) : décision 1 (a), 2 (a), 3 (b) au rejeu, 4 (b), 5 (a) au rejeu ; huit confirmations telles qu'écrites.
- Le programme qui lit les lectures : `JUGE/criteres-v5/assemblage_selection_v4_v2.py` (formes acceptées des lectures et des listes de veto, champ `lignee`, `lignee_reconnue`).
- Pour mémoire, les consignes ou rejeux antérieurs qui t'aident sans faire foi : `JUGE/rejeu-a-blanc-criteres-v2-lecteur-f-v1.md` et `JUGE/rejeu-a-blanc-criteres-v2-lecteur-o-v1.md` (notes seulement ; n'ouvre pas les fichiers de sélection).

## Ce que tu fais

1. **Consigne** (`consigne-lecteurs-rejeu-criteres-v7-v1.md`), une seule pour les deux lecteurs (lignée Opus et lignée Fable), qui dit : ce qu'ils reçoivent (les cartes masquées par le programme, jamais l'espèce ni `meta`) ; ce qu'ils rendent, au format exact de l'annexe A et sous la forme que le programme accepte ; le veto et sa liste (décision 2 (a) : plafond au nombre visé, retrait par famille) ; les questions « ajoutables » (décision 4 (b)) ; **la lignée reconnue, carte par carte (décision 3 (b)) : l'une des cinq étiquettes `prop-opus`, `prop-fable`, `prop-argon`, `prop-astra`, `prop-carbon`, lettre pour lettre, ou « aucune », dans les cartes comme dans les listes de veto** ; le champ `lignee` de chaque lecteur, lettre pour lettre ; ce que le lecteur ne fait jamais (trancher, adopter, ouvrir autre chose que les cartes servies). La consigne ne nomme aucun identifiant de modèle : elle nomme les lignées par leurs étiquettes.
2. **Rapport** (`rapport-redacteur-consigne-lecteurs-rejeu-v1.md`) : sources avec chemin et empreinte, ce que tu as vérifié dans le programme (fichier et ligne), ce qui reste ouvert.

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/redacteur-consigne-lecteurs-rejeu/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`). Le dossier courant n'est pas gardé : `env -C DOSSIER commande`.

## Interdits

Voir en tête. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucune carte. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Aucun fichier « consigne-privee » ni « conception-ii-b », ni `brouillons/ii-b-saboteur-budget-v1/`, ni la branche `lot/compte-4-v1`, ni la ligne R-2059. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
