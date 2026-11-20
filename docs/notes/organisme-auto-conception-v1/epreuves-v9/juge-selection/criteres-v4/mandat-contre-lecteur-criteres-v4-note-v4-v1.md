VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `grep -r`, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET, DONNÉ CI-DESSOUS OU CITÉ DANS UNE PIÈCE.

# Mandat du contre-lecteur — critères v4, note v4 et programmes du juge de sélection — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-20. Tu es un contre-lecteur neuf, modèle O : tu n'as écrit ni le mandat du rédacteur, ni les critères, ni la note, ni les programmes. Dossier : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/` (noté JUGE).

## Règle d'or, inchangée

Aucune carte ouverte, aucun fichier de cartes, aucun fichier de sélection (`selections-…json`), rien sous `archives-reponses-modeles/`. Tu ne lis jamais l'espèce d'une carte ni le champ `meta`.

## Ce que tu contre-lis (vérifie chaque empreinte contre son compagnon)

Dans `JUGE/criteres-v4/` : `criteres-choix-cartes-v9-v4.md` (`8e8c6194…`), `note-conception-juge-selection-cartes-ecartees-v4.md` (`4b2c5ad2…`), `assemblage_selection_v4_v1.py` (`258d5de7…`), `essais_assemblage_selection_v4_v1.py`, `masque_style_cartes_v1.py` (`07ed8725…`), `essais_masque_style_cartes_v1.py`, `lecteur_par_programme_cartes_v1.py` (`f656bd52…`), `essais_lecteur_par_programme_cartes_v1.py`, `mesure_faux_declenchement_gardes_v1.py`, `construire_par_lignes_v1.py`, `operations-criteres-v3-vers-v4-v1.txt`, `operations-note-v3-vers-v4-v1.txt`, les trois sorties d'essais (`essais-…-sortie-v1.txt`), `mesure-faux-declenchement-gardes-sortie-v1.txt`, `ecrire_compagnons_v1.py`, et le rapport `rapport-redacteur-criteres-v4-note-v4-v1.md` (`5530e316…`).

## Ce qui fait foi

- Le mandat du rédacteur : `JUGE/mandat-redacteur-criteres-v4-note-v4-v1.md` (`b7831779…`).
- `JUGE/contre-lecture-criteres-v3-note-v3-v1.md` (`cce1a8f4…`, les huit constats) ; `JUGE/audit-symetrie-rejeu-v2-v1.md` (`ff814fc9…`) ; `JUGE/criteres-choix-cartes-v9-v3.md` (`1ce41903…`) ; `JUGE/note-conception-juge-selection-cartes-ecartees-v3.md` (`de9d144d…`) ; `JUGE/statistique-famille-rejeu-v3-v1.md` (`bb2fa4a8…`), `JUGE/statistique_famille_rejeu_v3_v1.py`, `JUGE/contre-lecture-statistique-famille-rejeu-v3-v1.md`.
- `/home/user/controle-ia-travail/registres-provisoires/consignes-mere-epreuves-v9-compte-organisme-2026-11-19-v1.md` ; `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ordre-de-passage-epreuves-v9-v3.md`.
- Sur main (`git -C /home/user/controle-ia-travail fetch origin main` puis `git -C /home/user/controle-ia-travail show origin/main:CHEMIN`, redirigé vers ton dossier) : `registres/go.md` (GO-2026-11-19-55 à -74, -89), `docs/notes/organisme-auto-conception-v1/juge/litterature-juges-preference-pour-soi-v1.md`.

## Ce que tu vérifies

1. Les huit constats de `cce1a8f4…`, R-3876, GO-68, GO-69 et les recommandations de l'audit sont portés, chacun à sa place ; les v3 sont intactes, et les v4 sont bien la v3 plus les opérations déclarées (rejoue `construire_par_lignes_v1.py` sur les v3 dans ton dossier et compare à l'octet).
2. Les programmes : lance chaque fichier d'essais toi-même (`python3 -B -m pytest -q -p no:cacheprovider CHEMIN_DE_TA_COPIE`) ; chaque garde a un cas sain et un artefact (R5), aucun repli silencieux ; graines par `numpy.random.SeedSequence` (R9). Juge la réserve du cas sain de la garde (graine 8 choisie parce qu'elle ne déclenche pas) au regard de R4 et R5.
3. Les choix du rédacteur sont motivés et ne visent aucun signe (R3) : veto filtré par famille ; deux tests désignés d'avance à 0,025 ajoutés à la statistique de famille sans la réécrire ; masque coupé à la médiane.
4. N-058 et la parole de Lazar : un juge ne tranche jamais, il choisit seulement ce qui va à l'épreuve.
5. Les décisions pour Lazar sont au format ; les défauts des trois décisions du 19 vers 14:41Z sont justes (échéance le 21 vers 14:41Z).
6. Les noms de lignées des juges (« Opus », « Fable », « Argon », « Carbon ») sont des étiquettes de famille déjà présentes dans les v3 scellées, pas des identifiants de modèle ; signale seulement un identifiant de modèle véritable.

Verdict : « Conforme », « Conforme après corrections » (liste exacte, texte ancien et nouveau ; elles seront appliquées par un rédacteur de modèle F) ou « Non conforme ».

## Ce que tu rends

Dans `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/contre-lecture-juge-v4/` : `contre-lecture-criteres-v4-note-v4-v1.md` et son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`). Signe « contre-lecteur, modèle O ». Le dossier courant n'est pas gardé : `env -C DOSSIER commande` ; copies fichier par fichier, chemins complets.

## Interdits

Aucune commande de liste (voir en tête). Jamais de heredoc ni de code en ligne passé à un interpréteur ; une commande simple à la fois. Aucune écriture dans le dépôt, aucun commit. Aucune carte, aucune commande sur un chemin sous `archives-reponses-modeles/`. Aucun fichier « consigne-privee » ni « conception-ii-b », ni `brouillons/ii-b-saboteur-budget-v1/`, ni la branche `lot/compte-4-v1`, ni la ligne R-2059, ni `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Au premier refus d'un outil ou d'un classifieur : arrête-toi et dis-le.
