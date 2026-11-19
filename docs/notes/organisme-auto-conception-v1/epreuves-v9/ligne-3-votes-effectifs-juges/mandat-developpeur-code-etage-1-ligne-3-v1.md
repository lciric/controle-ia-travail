# Mandat du développeur — code de l'étage 1 de la ligne 3 (banc de juges scriptés, processeur seul ; classe B) — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-19 vers 23:00Z, sur le scellement de la ligne 3 v7 par la mère (clés `PREREG-ORGANISME-V9-LIGNE-3` et `DEVIS-ORGANISME-V9-LIGNE-3`, registre des scellements ; R-4000) et l'ordre des gestes du texte scellé (geste 3).

## Ce qui fait foi

Le préenregistrement scellé : `prereg/organisme-auto-conception-v9/preenregistrement-ligne-3-votes-effectifs-juges-v7.md` sur main, sha256 `4e3680d9915ef6e2fa33010fc9b7b2ef5575d74e58e982bfabdbdbcc3e99d5a0` (lis-le par `git show origin/main:CHEMIN` après `git fetch origin main`). Sections : « 0 », « Métrique », « Seuil », « Plan d'analyse », **Étage 1** seulement, « Graines (règle R9), ordre des gestes », « Critères de lecture gelés », « Liste d'arrêt », **Annexe A**. Le calcul des prédictions v2 (`ligne-3-votes-effectifs-juges/calcul_predictions_ligne_3_v2.py`, sortie `2cf1eba7…`) sert de référence aux essais de formules.

## Ce que tu fais

Tu écris, **pour l'étage 1 seulement**, ce que l'annexe A nomme : `banc_juges_scriptes_ligne_3_v1.py` et `essais_banc_juges_scriptes_ligne_3_v1.py`, plus le chronométrage qui n'imprime que des durées. Rien de l'étage 2 (ni générateur de témoins, ni garde de recouvrement, ni épreuve sur juges réels, ni compteur d'arrêt) : ces pièces viennent au geste 6, après la lecture de l'étage 1.

- Graines : `numpy.random.SeedSequence(racine, spawn_key=(clé,))`, clé entière, table « tâche → entier » gelée dans le code et recopiée au manifeste ; racines du texte : essais **2026111930** ; chronométrage 2026111931 ; étage 1 décisif 2026111932 ; rééchantillonnage 2026111933. Pendant ton travail, **seule la racine des essais 2026111930** est dérivée ; les racines décisives lèvent un refus sans autorisation. Écris l'essai final qui contrôle qu'aucune graine des racines 2026111931 à 2026111937 n'a été dérivée dans le processus des essais.
- Un manifeste par exécution (R9) : configuration et empreinte, versions, graines, commit.
- Essais : chaque garde de la liste d'arrêt qui touche l'étage 1, cas sain et artefact (R5) ; les essais de formules de l'annexe A (grand n, corrélation estimée contre valeur plantée par loi ; erreur équilibrée contre les formules du § 0 ; taux exacts du double rendu et écarts vrais du monde de puissance contre le calcul des prédictions). Contrôle « trop beau » (R4) : défauts réintroduits un par un dans une copie, vus par l'essai visé.
- Python `/usr/local/bin/python3`, numpy et la bibliothèque standard ; pas de scipy.
- Où : sous `docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/code-etage-1-v1/`, avec un rapport `rapport-developpeur-code-etage-1-ligne-3-v1.md`.

Où le texte se tait, comble par le choix le plus étroit et déclare-le ; ne tranche rien de ce qui est jugé ou lu : liste ces points pour la mère.

## Outil fourni

Pour tout remplacement de texte dans un fichier, utilise l'outil contre-lu du dépôt : `python3 -B scripts/remplacer_texte_exact_v1.py --cible F --remplacements R.json --sortie NOUVEAU` (empreinte `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6`, contre-lecture « Conforme »). Il refuse un texte ancien absent ou multiple, et un neuf recréé par jonction : élargis alors le contexte.

## Interdits

**Jamais de heredoc ni de bloc de texte ou de code en ligne passé à un interpréteur (ni `python3 -c`, ni `python3 -`)** : écris tout programme dans un fichier et lance-le par son chemin ; un développeur précédent a été arrêté pour cela. Ne lance jamais l'étage 1 décisif ni le chronométrage décisif (geste 4, après l'additif de code scellé). Aucun appel à un fournisseur de modèles, aucune dépense, aucune machine, aucun réseau sauf `git fetch`/`git show` du dépôt. Aucun commit, aucune poussée. Aucune valeur de clé. **Aucune commande, même une empreinte, une liste ou une taille, sur un chemin sous `archives-reponses-modeles/`.** Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif dans une commande, même pour une attente. Aucun identifiant de modèle ; signe « développeur, modèle L′ ». Au premier refus d'un outil de la session : arrête-toi et dis-le.
