VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

# Mandat du rédacteur — épreuve sur l'héritage, préenregistrement du palier 0b, version 5 (erratum) — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-19 vers 23:41Z, sur GO-2026-11-19-84 et -93 et le choix de la mère (vers 23:38Z).

## Ce que tu fais

Tu écris la version 5 du préenregistrement du palier 0b (`preenregistrement-heritage-palier-0b-etage-processeur-v5.md`), à partir de la version 4 (`d5b817d3…`, intacte, R12), limitée aux **quatre corrections** de la relecture `heritage/palier-0b/relecture-preenregistrement-palier-0b-v4-v1.md` (`4cc14afe…`), appliquées **à la lettre** avec les textes exacts de son § 6 :
1. **retenue par la mère** : les exactitudes sur les traits de forme décident ; celles sur les traits de contenu sont rapportées sans arrêter au palier 0b et lient l'étage payant (au-delà de 0,55, générateur revu et réaudité par erratum avant tout préenregistrement payant) ; adapter la garde 25, la réserve 18 et l'annexe F comme la relecture le dit ;
2. garde 25 : cas sain « bornes gelées, générateur sain : aucun arrêt » et artefact « un tirage par loi et un essai par monde : arrêt nommé « bornes de la construction épuisées » » (R5) ;
3. une huitième fréquence pour les lois vraies du monde source, distincte de celle des mondes cibles, dans M12, S8, l'annexe C et l'annexe F ; le nombre de lois par strate rapporté avec l'intervalle exact de sa fréquence ;
4. l'audit des mondes par dose lu par paires de doses (0 contre 0,25 ; 0 contre 0,5 ; 0,25 contre 0,5), seuil inchangé.

Plus la tenue (titre, statut, heure, mandat cité, relecture citée, section de différentiel v4 → v5). Rien d'autre ne change.

Applique les remplacements avec l'outil contre-lu `python3 -B scripts/remplacer_texte_exact_v1.py --cible F --remplacements R.json --sortie NOUVEAU` (empreinte `391db990…`) ; il refuse un ancien absent ou multiple, ou un neuf recréé par jonction : élargis alors le contexte. Produis le différentiel v4 → v5.

## Ce que tu lis

`CLAUDE.md` ; la version 4, son rapport, son mandat ; la relecture `4cc14afe…`. Vérifie chaque empreinte avant de citer.

## Ce que tu rends

Dans ton bloc-notes seulement : la version 5, `differentiel-preenregistrement-palier-0b-v4-v5.diff`, `rapport-redacteur-palier-0b-v5-v1.md` (court), ton JSON de remplacements. En-tête : « Auteur : rédacteur neuf, modèle F » ; aucun identifiant de modèle ; heure par `date -u`.

## Interdits

Jamais de heredoc ni de bloc de texte ou de code en ligne passé à un interpréteur, même vide. Une commande simple à la fois. Aucun tirage, aucun lancement du code versé. Aucun appel à un fournisseur de modèles, aucune dépense, aucune machine, aucun réseau sauf `git fetch`/`git show` du dépôt. Aucun commit, aucune poussée, aucune écriture dans le dépôt. Aucune valeur de clé. **Aucune commande, même une empreinte, une liste ou une taille, sur un chemin sous `archives-reponses-modeles/`.** Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif dans une commande. Au premier refus d'un outil : arrête-toi et dis-le.
