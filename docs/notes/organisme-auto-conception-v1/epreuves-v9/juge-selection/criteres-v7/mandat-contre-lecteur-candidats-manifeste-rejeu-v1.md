VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat du contre-lecteur des critères — quatre fichiers candidats du manifeste du rejeu du juge — v1

Pièce de travail (classe C). Donnée par la session du compte organisme le 2026-11-20, sur la demande de la mère (après R-4128, vérification X6 close : 94 clés, aucune des deux retenues présente). Pour le contre-lecteur, modèle O, auteur de la table du manifeste (`a41a2c7c…`). **Rien n'est scellé de ton côté** : la mère relit, rejoue `valider_manifeste` et scelle.

Dossier J = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/`.

## Ce qui fait foi (seulement des pièces scellées et ta table corrigée ; vérifie chaque empreinte)

- Ta table : `J/criteres-v7/table-manifeste-rejeu-apres-go-2026-11-20-10-v1.md` (`a41a2c7c…`), avec la correction de forme X6 de son § (c) : `hors_choix` = `[]`, `cartes_attendues` = 94.
- Sur main (`fetch`, puis `git show` redirigé) : critères v7 (`6af793a2…`) et note v7 (`bbd71b7c…`) sous `prereg/organisme-auto-conception-v9/juge-selection/` ; `registres/go.md` (GO-2026-11-20-10, point O2) ; `registres/decisions.md` (R-4097, R-4102, R-4128) ; la garde `docs/notes/organisme-auto-conception-v9-mere/juge-selection-manifeste-v1/garde_lignee_reconnue_v2.py` (`635e9160…`) ; l'extraction X6 `docs/notes/organisme-auto-conception-v9-mere/juge-selection-x6-v1/sortie-extraction-x6-v2.json` (`f5c7cc1c…`), pièce de la mère, dont tu ne lis que `extraction.identifiants_par_classe.a_corriger`.
- Le rapport v7 : `J/criteres-v7/rapport-redacteur-corrections-criteres-v7-note-v7-v1.md` (`2a12a78f…`), § 5 (configurations), C1 à C3, décision 5 (a), confirmation 8.
- Les familles : `J/criteres-v7/reponses-familles-et-champ-x6-v1.md` (`35cc9bcf…`).
- Le programme : `J/criteres-v5/assemblage_selection_v4_v2.py` (`2f5640da…`), `CLES_MANIFESTE` et `valider_manifeste` (l. 113).
- La vérification X6 close : `J/verification-x6-fiches-v1/second-jeu-v1/resultat-verification-x6-v2.json`.

## Ce que tu fais

Tout fichier JSON s'écrit **par un programme** que tu écris dans ton dossier (outil d'écriture de fichiers, jamais de code en ligne), qui part des valeurs de ta table et des pièces ci-dessus ; aucune valeur tapée à la main dans un JSON.

1. `manifeste-rejeu-v1.json` : les seize clés de `CLES_MANIFESTE`, mêmes valeurs que ta table, plus son § (c) : `hors_choix` = `[]`, `cartes_attendues` = 94, `familles` avec les cinq étiquettes, Argon et Carbon dans deux familles distinctes. Ton programme importe `assemblage_selection_v4_v2.py` (pris à son empreinte) et appelle `valider_manifeste` ; joins la sortie entière (`sortie-valider-manifeste-v1.txt`).
2. `configuration-a-masque-v1.json` et `configuration-b-lecteur-v1.json`, selon le § 5 du rapport v7, avec C1 à C3, la décision 5 (a) et la confirmation 8. Si le programme a une fonction de validation de configuration, appelle-la et joins sa sortie.
3. `brouillon-piece-scellement-manifeste-rejeu-v1.md`, au nom de la mère, en brouillon : la justification de chaque valeur (M1), la citation de GO-2026-11-20-10 (O2), les deux identifiants X6 avec R-4097, R-4102 et R-4128, la garde de `lignee_reconnue` v2 (`635e9160…`), et les réserves (celles de ta table, § « Réserves », chacune dite levée ou ouverte au vu de R-4128). La mère cite aussi « la réserve de ton § 4 » : si tu ne sais pas laquelle, dis-le en tête du brouillon au lieu de deviner.
4. Un rapport court `rapport-candidats-manifeste-rejeu-v1.md` : fichiers et empreintes, programmes et commandes, sortie de `valider_manifeste`, tout écart.

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/candidats-manifeste-rejeu-v1/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête. **Aucune carte, rien sous `archives-reponses-modeles/`**, par aucune commande. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucune écriture dans le dépôt, aucun commit, aucun scellement. Rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
